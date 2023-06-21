from datetime import date, datetime
from typing import Dict, List, Optional

from pydantic import BaseModel, Field

from huntflow_webhook_models.consts import VacancyState


class FillQuota(BaseModel):
    id: int = Field(..., description="Fill quota ID", example=1)
    applicants_to_hire: int = Field(..., description="Amount of applicant to hire", example=1)
    closed: Optional[datetime] = Field(
        None,
        description="Date time the fill quota was closed",
        example=datetime(1970, 1, 1, 1, 1, 1),
    )
    created: datetime = Field(
        ...,
        description="Date time the fill quota was created",
        example=datetime(1970, 1, 1, 1, 1, 1),
    )
    deadline: Optional[date] = Field(
        None,
        description="Fill quota deadline",
        example=date(1970, 1, 1),
    )
    vacancy_request: Optional[int] = Field(
        None,
        description="Fill quota vacancy request",
        example=1,
    )


class AccountDivision(BaseModel):
    id: int = Field(..., description="Account division ID", example=1)
    name: str = Field(..., description="Account division name", example="IT Department")


class Vacancy(BaseModel):
    id: int = Field(..., description="Vacancy ID", example=1)
    account_division: Optional[AccountDivision] = Field(
        None,
        description="Vacancy account division",
    )
    account_region: Optional[int] = Field(None, description="Vacancy region ID", example=1)
    applicant_to_hire: Optional[int] = Field(
        None,
        description="Amount applicants to hire",
        example=1,
    )
    body: Optional[str] = Field(
        None,
        description="Vacancy responsibilities (HTML)",
        example="<p>Be happy</p>",
    )
    company: Optional[str] = Field(None, description="Vacancy company", example="Huntflow")
    conditions: Optional[str] = Field(
        None,
        description="Vacancy conditions(HTML)",
        example="<p>Big salary</p>",
    )
    created: date = Field(
        ...,
        description="Date the vacancy was created",
        example=datetime(1970, 1, 1, 1, 1, 1),
    )
    deadline: Optional[date] = Field(..., description="Vacancy deadline", example=date(1970, 1, 1))
    fill_quotas: List[FillQuota] = Field([], description="Vacancy fill quota")
    frame_id: int = Field(..., description="Vacancy frame ID", example=1)
    hidden: bool = Field(..., description="Hidden vacancy flag", example=True)
    money: Optional[str] = Field(None, description="Salary for vacancy", example="100000")
    multiple: bool = Field(..., description="Multiple vacancy flag", example=False)
    parent: Optional[int] = Field(None, description="Vacancy parent ID", example=1)
    position: str = Field(..., description="Vacancy position", example="Python developer")
    priority: int = Field(..., description="Vacancy priority", example=1)
    requirements: Optional[str] = Field(
        None,
        description="vacancy requirements(HTML)",
        example="<p>Work responsibly</p>",
    )
    state: VacancyState = Field(..., description="Vacancy state", example=VacancyState.OPEN)
    values: Dict = Field(
        {},
        description="Additional vacancy fields",
        example={"experience": "without"},
    )


class VacancyLog(BaseModel):
    id: int = Field(..., description="Vacancy log ID", example=1)
    type_: VacancyState = Field(
        ...,
        alias="type",
        description="Vacancy log state",
        example=VacancyState.OPEN,
    )
    created: datetime = Field(
        ...,
        description="Date time the vacancy log created",
        example=datetime(1970, 1, 1, 1, 1, 1),
    )
    reason: Optional[str] = Field(
        None,
        description="Vacancy rejection reason",
        example="Do not take to work",
    )
