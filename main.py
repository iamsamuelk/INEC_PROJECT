from fastapi import FastAPI, HTTPException, Depends
from fastapi.templating import Jinja2Templates
from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker, Session
from models import AnnouncedPUResults, PollingUnit

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Database connection
SQLALCHEMY_DATABASE_URL = (
    "postgresql://vgsykulb:xsMjB35xK8R5wiNakTbmdl0pB8PY5tQk@"
    "drona.db.elephantsql.com/vgsykulb"
)
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

@app.get("/polling_unit/{polling_unit_id}")
async def read_polling_unit_result(
    polling_unit_id: int,
    db: Session = Depends(get_db)
):
    results = db.query(AnnouncedPUResults).filter(
        AnnouncedPUResults.polling_unit_uniqueid == str(polling_unit_id)
    ).all()
    if not results:
        raise HTTPException(status_code=404, detail="Polling unit not found")
    return results


# Route to display summed total result of all polling units under an lga


