from datetime import date, datetime
from typing import Optional

from pydantic import BaseModel, Field


class AccountFile(BaseModel):
    id: int = Field(..., description="File ID", examples=[1])
    content_type: str = Field(..., description="MIME type", examples=["image/jpeg"])
    name: str = Field(..., description="Filename", examples=["test_file.jpeg"])
    url: str = Field(..., description="File url", examples=["https://domain/file/1"])


class AccountInfo(BaseModel):
    id: int = Field(..., description="Account ID", examples=[1])
    name: str = Field(..., description="Account owner name", examples=["John"])
    email: Optional[str] = Field(
        None,
        description="Account owner email",
        examples=["test@email.com"],
    )


class AccountSource(BaseModel):
    id: int = Field(..., description="Resume source ID", examples=[1])
    foreign: Optional[str] = Field(
        None,
        description="Applicant source foreign",
        examples=["f2"],
    )
    name: str = Field(..., description="Applicant source name", examples=["Headhunter"])
    type: str = Field(..., description="Applicant source type", examples=["user"])


class VacancyQuotaBase(BaseModel):
    id: int = Field(..., description="Fill quota ID")
    vacancy_frame: int = Field(..., description="Vacancy frame ID")
    vacancy_request: Optional[int] = Field(None, description="Vacancy request ID")
    created: datetime = Field(..., description="Date and time of creating a vacancy quota")
    changed: Optional[datetime] = Field(
        None,
        description="Date and time of updating a vacancy quota",
    )
    applicants_to_hire: int = Field(
        ...,
        description="Number of applicants should be hired on the quota",
    )
    already_hired: int = Field(..., description="Number of applicants already hired on the quota")
    deadline: Optional[date] = Field(None, description="Date when the quota should be filled")
    closed: Optional[datetime] = Field(None, description="Date and time when the quota was closed")
    work_days_in_work: Optional[int] = Field(
        None,
        description="How many working days the vacancy is in work",
    )
    work_days_after_deadline: Optional[int] = Field(
        None,
        description="How many working days the vacancy is in work after deadline",
    )
    work_days_before_deadline: Optional[int] = Field(
        None,
        description="How many working days the vacancy is in work before deadline",
    )


class VacancyQuotaItem(VacancyQuotaBase):
    account_info: AccountInfo
