from fastapi import HTTPException, status
from fastapi.templating import Jinja2Templates
from sqlalchemy import func, cast, Integer
from sqlalchemy.orm import Session
from models import PollingUnit, AnnouncedPUResults, LGA
import schema
from datetime import datetime

templates = Jinja2Templates(directory="templates")


def get_polling_unit_results(db: Session, polling_unit_name: str):
    polling_unit = db.query(PollingUnit).filter(
        PollingUnit.polling_unit_name == polling_unit_name
    ).first()
    if not polling_unit:
        return templates.TemplateResponse(
            "home.html",
            status_code=status.HTTP_302_FOUND
        )

    results = db.query(AnnouncedPUResults).filter(
        cast(AnnouncedPUResults.polling_unit_uniqueid, Integer) ==
        PollingUnit.uniqueid
    ).all()
    if not results:
        return {
            "error": "No results found for the selected polling unit",
            "polling_unit_name": polling_unit_name
        }
    return results


def get_lga_results(db: Session, lga_name: str):
    try:
        lga = db.query(LGA).filter(LGA.lga_name == lga_name).first()
        if not lga:
            raise HTTPException(status_code=404, detail="LGA not found")

        results = db.query(
            AnnouncedPUResults.party_abbreviation,
            func.sum(AnnouncedPUResults.party_score).label('total_score')
        ).join(
            PollingUnit,
            (
                cast(AnnouncedPUResults.polling_unit_uniqueid, Integer) ==
                PollingUnit.uniqueid
            )
        ).filter(
            PollingUnit.lga_id == lga.lga_id
        ).group_by(
            AnnouncedPUResults.party_abbreviation
        ).all()

        if not results:
            return {
                "error": "No results found for the selected LGA",
                "lga_name": lga_name
            }

        # Convert query results to list of dictionaries
        formatted_results = [
            {"party_abbreviation": party, "total_score": score}
            for party, score in results
        ]

        return formatted_results
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


def get_polling_unit(db: Session, polling_unit_uniqueid: int):
    return db.query(PollingUnit).filter(
        PollingUnit.uniqueid == polling_unit_uniqueid
    ).first()


def create_polling_unit_result(
    db: Session,
    result: schema.PollingUnitResult,
    date_entered: datetime,
    user_ip_address: str
):
    new_result = AnnouncedPUResults(
        polling_unit_uniqueid=result.polling_unit_uniqueid,
        party_abbreviation=result.party_abbreviation,
        party_score=result.party_score,
        entered_by_user=result.entered_by_user,
        date_entered=date_entered,
        user_ip_address=user_ip_address
    )
    db.add(new_result)
    db.commit()
    db.refresh(new_result)
    return new_result
