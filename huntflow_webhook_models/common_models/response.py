from datetime import datetime
from typing import Optional

from pydantic.fields import Field
from pydantic.main import BaseModel

from huntflow_webhook_models.common_models.hf_base import AccountSource
from huntflow_webhook_models.common_models.vacancy import Vacancy
from huntflow_webhook_models.consts import (
    ApplicantResponseExternalStatus,
    VacancyExternalPublishStatus,
)


class ApplicantExternalResponse(BaseModel):
    id: int = Field(..., description="Applicant source ID", examples=[1])
    created: datetime = Field(
        ...,
        description="The datetime when the response was stored in the database",
        examples=[datetime(1970, 1, 1, 1, 1, 1)],
    )
    foreign: str = Field(
        ...,
        description="Foreign applicant external ID",
        examples=["external-9-23"],
    )
    resume: Optional[dict] = Field(None, description="Applicant resume")
    state: Optional[ApplicantResponseExternalStatus] = Field(
        None,
        description="Response state",
        examples=[ApplicantResponseExternalStatus.TAKEN],
    )
    updated: datetime = Field(
        ...,
        description="Datetime of response creation/update on the career site",
        examples=[datetime(1980, 1, 1, 1, 1, 1)],
    )


class AccountVacancyExternal(BaseModel):
    id: int = Field(..., description="Account vacancy external ID", examples=[1])
    account_source: AccountSource = Field(..., description="Vacancy account source")
    auth_type: str = Field(..., description="Authentication type", examples=["NATIVE"])
    name: str = Field(..., description="Account vacancy external name", examples=["HeadHunter"])


class VacancyExternal(BaseModel):
    id: int = Field(..., description="Vacancy external ID", examples=[1])
    account_vacancy_external: AccountVacancyExternal = Field(
        ...,
        description="Account vacancy external",
    )
    data: str = Field(
        ...,
        description="Additional data",
        examples=["Developer"],
    )
    foreign: str = Field(..., description="Foreign vacancy external ID", examples=["12345"])
    state: Optional[VacancyExternalPublishStatus] = Field(
        None,
        description="Vacancy external publish status",
        examples=[VacancyExternalPublishStatus.PUBLISHED],
    )
    vacancy: Vacancy = Field(..., description="Vacancy data")
