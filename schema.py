from pydantic import BaseModel


class PollingUnitResult(BaseModel):
    polling_unit_uniqueid: int
    party_abbreviation: str
    party_score: int
    entered_by_user: str


class PollingUnitResults(BaseModel):
    results: list[PollingUnitResult]
