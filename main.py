from fastapi import FastAPI, Request, HTTPException, Depends
from fastapi.templating import Jinja2Templates
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from models import PollingUnit, AnnouncedPUResults

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Database connection
SQLALCHEMY_DATABASE_URL = "sqlite:///bincom_test.sql"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Dependency to get a database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Route to display polling unit result
@app.get("/polling_unit/{unit_id}")
async def get_polling_unit_result(
    unit_id: int, request: Request, db: Session = Depends(get_db)
):
    polling_unit = db.query(PollingUnit).filter(
        PollingUnit.polling_unit_id == unit_id
    ).first()
    if not polling_unit:
        raise HTTPException(status_code=404, detail="Polling unit not found")
    results = db.query(AnnouncedPUResults).filter(
        AnnouncedPUResults.polling_unit_uniqueid == unit_id
    ).all()
    return templates.TemplateResponse(
        "polling_unit_result.html",
        {"request": request, "polling_unit": polling_unit, "results": results},
    )
