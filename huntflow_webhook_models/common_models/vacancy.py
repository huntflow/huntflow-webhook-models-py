from datetime import date, datetime
from typing import Dict, List, Optional

from pydantic import BaseModel, Field

from huntflow_webhook_models.consts import VacancyState


class FillQuota(BaseModel):
    id: int = Field(..., description="Fill quota ID", examples=[1])
    applicants_to_hire: int = Field(..., description="Amount of applicant to hire", examples=[1])
    closed: Optional[datetime] = Field(
        None,
        description="Date time the fill quota was closed",
        examples=[datetime(1970, 1, 1, 1, 1, 1)],
    )
    created: datetime = Field(
        ...,
        description="Date time the fill quota was created",
        examples=[datetime(1970, 1, 1, 1, 1, 1)],
    )
    deadline: Optional[date] = Field(
        None,
        description="Fill quota deadline",
        examples=[date(1970, 1, 1)],
    )
    vacancy_request: Optional[int] = Field(
        None,
        description="Fill quota vacancy request",
        examples=[1],
    )


class AccountRegion(BaseModel):
    id: int = Field(..., description="Account region ID", examples=[1])
    name: str = Field(..., description="Account region name", examples=["Turkey"])


class AccountDivision(BaseModel):
    id: int = Field(..., description="Account division ID", examples=[1])
    name: str = Field(..., description="Account division name", examples=["IT Department"])


class Vacancy(BaseModel):
    id: int = Field(..., description="Vacancy ID", examples=[1])
    account_division: Optional[AccountDivision] = Field(
        None,
        description="Vacancy account division",
    )
    account_region: Optional[AccountRegion] = Field(None, description="Account region")
    applicants_to_hire: Optional[int] = Field(
        None,
        description="Amount applicants to hire",
        examples=[1],
    )
    body: Optional[str] = Field(
        None,
        description="Vacancy responsibilities (HTML)",
        examples=["<p>Be happy</p>"],
    )
    company: Optional[str] = Field(None, description="Vacancy company", examples=["Huntflow"])
    conditions: Optional[str] = Field(
        None,
        description="Vacancy conditions(HTML)",
        examples=["<p>Big salary</p>"],
    )
    created: date = Field(
        ...,
        description="Date the vacancy was created",
        examples=[date(1970, 1, 1)],
    )
    deadline: Optional[date] = Field(
        None,
        description="Vacancy deadline",
        examples=[date(1970, 1, 1)],
    )
    fill_quotas: List[FillQuota] = Field([], description="Vacancy fill quota")
    frame_id: int = Field(..., description="Vacancy frame ID", examples=[1])
    hidden: bool = Field(..., description="Hidden vacancy flag", examples=[True])
    money: Optional[str] = Field(None, description="Salary for vacancy", examples=["100000"])
    multiple: bool = Field(..., description="Multiple vacancy flag", examples=[False])
    parent: Optional["Vacancy"] = Field(None, description="Parent vacancy")
    position: str = Field(..., description="Vacancy position", examples=["Python developer"])
    priority: int = Field(..., description="Vacancy priority", examples=[1])
    requirements: Optional[str] = Field(
        None,
        description="vacancy requirements(HTML)",
        examples=["<p>Work responsibly</p>"],
    )
    state: VacancyState = Field(..., description="Vacancy state", examples=[VacancyState.OPEN])
    values: Dict = Field(
        {},
        description="Additional vacancy fields",
        examples=[{"experience": "without"}],
    )


class VacancyCloseReason(BaseModel):
    id: int = Field(..., description="Vacancy close reason ID", examples=[1])
    name: str = Field(..., description="Vacancy close reason name", examples=["All hired"])


class VacancyHoldReason(BaseModel):
    id: int = Field(..., description="Vacancy hold reason ID", examples=[1])
    name: str = Field(..., description="Vacancy hold reason name", examples=["Cancel budget"])


class VacancyLog(BaseModel):
    id: int = Field(..., description="Vacancy log ID", examples=[1])
    state: VacancyState = Field(
        ...,
        description="Vacancy log state",
        examples=[VacancyState.OPEN],
    )
    created: datetime = Field(
        ...,
        description="Date time the vacancy log created",
        examples=[datetime(1970, 1, 1, 1, 1, 1)],
    )
    close_reason: Optional[VacancyCloseReason] = Field(
        None,
        description="Vacancy close reason",
        examples=[""],
    )
    hold_reason: Optional[VacancyHoldReason] = Field(
        None,
        description="Vacancy hold reason",
        examples=[""],
    )
