from fastapi import HTTPException
from sqlalchemy import func, cast, Integer
from sqlalchemy.orm import Session
from models import PollingUnit, AnnouncedPUResults
import schema
from datetime import datetime


def get_pu_results(db: Session, polling_unit_id: int,):
    results = db.query(AnnouncedPUResults).filter(
        cast(AnnouncedPUResults.polling_unit_uniqueid, Integer) ==
        polling_unit_id
    ).all()
    if not results:
        raise HTTPException(status_code=404, detail="Polling unit not found")
    return results


def get_lga_results(db: Session, lga_id: int):
    try:
        results = db.query(
            AnnouncedPUResults.party_abbreviation,
            func.sum(AnnouncedPUResults.party_score).label('total_score')
        ).join(
            PollingUnit,
            (cast(AnnouncedPUResults.polling_unit_uniqueid, Integer) ==
             PollingUnit.uniqueid)
        ).filter(
            PollingUnit.lga_id == lga_id
        ).group_by(
            AnnouncedPUResults.party_abbreviation
        ).all()

        if not results:
            raise HTTPException(
                status_code=404,
                detail="LGA not found or no results available"
            )

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
