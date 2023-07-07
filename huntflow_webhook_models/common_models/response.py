from datetime import datetime
from typing import Any, Dict, Optional

from pydantic.fields import Field
from pydantic.main import BaseModel

from huntflow_webhook_models.common_models.hf_base import AccountSource
from huntflow_webhook_models.common_models.vacancy import Vacancy
from huntflow_webhook_models.consts import (
    ApplicantResponseExternalStatus,
    VacancyExternalPublishStatus,
)


class ApplicantExternalResponse(BaseModel):
    id: int = Field(..., description="Applicant source ID", example=1)
    created: datetime = Field(
        ...,
        description="The datetime when the response was stored in the database",
        example=datetime(1970, 1, 1, 1, 1, 1),
    )
    data: Dict[str, Any] = Field(
        ...,
        description="Additional data",
        example={"body": "lorem ipsum body for 23"},
    )
    foreign: str = Field(..., description="Foreign applicant external ID", example="external-9-23")
    resume: Optional[Dict[str, Any]] = Field(None, description="Applicant resume")
    state: Optional[ApplicantResponseExternalStatus] = Field(
        None,
        description="Response state",
        example=ApplicantResponseExternalStatus.TAKEN,
    )
    updated: datetime = Field(
        ...,
        description="Datetime of response creation/update on the career site",
        example=datetime(1980, 1, 1, 1, 1, 1),
    )


class AccountVacancyExternal(BaseModel):
    id: int = Field(..., description="Account vacancy external ID", example=1)
    account_source: AccountSource = Field(..., description="Vacancy account source")
    auth_type: str = Field(..., description="Authentication type", example="NATIVE")
    name: str = Field(..., description="Account vacancy external name", example="Some site")


class VacancyExternal(BaseModel):
    id: int = Field(..., description="Vacancy external ID", example=1)
    account_vacancy_external: AccountVacancyExternal
    created: datetime = Field(
        ...,
        description="The datetime when the vacancy was stored in the database",
        example=datetime(1970, 1, 1, 1, 1, 1),
    )
    data: str = Field(
        ...,
        description="Additional data",
        example="comment",
    )
    foreign: str = Field(..., description="Foreign vacancy external ID", example="12345")
    state: Optional[VacancyExternalPublishStatus] = Field(
        None,
        description="Vacancy external publish status",
        example=VacancyExternalPublishStatus.PUBLISHED,
    )
    vacancy: Vacancy
