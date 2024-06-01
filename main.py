from fastapi import FastAPI, Depends, HTTPException, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from datetime import datetime
import crud
import schema
import socket

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")


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


# Home route
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})


# Route to render polling_unit.html
@app.get("/polling_unit", response_class=HTMLResponse)
async def get_polling_unit_page(request: Request):
    return templates.TemplateResponse(
        "polling_unit.html",
        {"request": request}
    )


# Route to display polling unit result
@app.get("/polling_unit/{polling_unit_name}")
async def read_polling_unit_result(
    request: Request,
    polling_unit_name: str,
    db: Session = Depends(get_db)
):
    results = crud.get_polling_unit_results(db, polling_unit_name)
    if "error" in results:
        return templates.TemplateResponse("lga_results.html", {
            "request": request,
            "polling_unit_name": polling_unit_name,
            "error": results["error"]
        })
    return templates.TemplateResponse("polling_unit.html", {
        "request": request,
        "polling_unit_name": polling_unit_name,
        "results": results
    })


# Route to render lga_results.html
@app.get("/lga_results", response_class=HTMLResponse)
async def get_lga_results_page(request: Request):
    return templates.TemplateResponse("lga_results.html", {"request": request})


# Route to display summed total result of all polling units under an lga
@app.get("/lga_results/{lga_name}")
async def read_lga_results(
    request: Request, lga_name: str, db: Session = Depends(get_db)
):
    results = crud.get_lga_results(db, lga_name)
    if "error" in results:
        return templates.TemplateResponse("lga_results.html", {
            "request": request,
            "lga_name": lga_name,
            "error": results["error"]
        })
    return templates.TemplateResponse("lga_results.html", {
        "request": request,
        "lga_name": lga_name,
        "results": results
    })


#  Route to store new results for polling units
@app.post("/add_polling_unit_results/", response_model=dict)
def add_polling_unit_results(results: schema.PollingUnitResults,
                             db: Session = Depends(get_db)):
    for result in results.results:
        # Check if the polling unit exists
        polling_unit = crud.get_polling_unit(db, result.polling_unit_uniqueid)
        if not polling_unit:
            raise HTTPException(
                status_code=404,
                detail=("Polling unit with id "
                        + f"{result.polling_unit_uniqueid} not found")
            )

        # Create a new result entry
        crud.create_polling_unit_result(
            db=db,
            result=result,
            date_entered=datetime.now(),
            user_ip_address=socket.gethostbyname(socket.gethostname())
        )

    return {"message": "Results added successfully"}
