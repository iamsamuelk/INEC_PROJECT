from pydantic import BaseModel
from typing import List


class PollingUnitResult(BaseModel):
    polling_unit_uniqueid: int
    party_abbreviation: str
    party_score: int
    entered_by_user: str


class PollingUnitResults(BaseModel):
    results: List[PollingUnitResult]
