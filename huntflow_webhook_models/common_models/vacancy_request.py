import datetime
from typing import Any, Dict

from pydantic import BaseModel, Field

from huntflow_webhook_models.consts import VacancyRequestLogAction


class VacancyRequest(BaseModel):
    id: int = Field(..., description="Vacancy request ID", example=1)
    account_vacancy_request: int = Field(..., description="Account vacancy request ID", example=1)
    created: datetime.datetime = Field(
        ...,
        description="Date time vacancy request created",
        example=datetime.datetime(1970, 1, 1, 1, 1, 1),
    )
    position: str = Field(..., description="Vacancy position", example="Developer")
    values: Dict[str, Any] = Field(
        ...,
        description="Vacancy request fields",
        example={"company": "test_company"},
    )


class VacancyRequestLog(BaseModel):
    id: int = Field(..., description="Vacancy request log ID", example=1)
    action: VacancyRequestLogAction = Field(
        ...,
        description="Vacancy request log action",
        example=VacancyRequestLogAction.CREATE,
    )
    created: datetime.datetime = Field(
        ...,
        description="Date time vacancy request log created",
        example=datetime.datetime(1970, 1, 1, 1, 1, 1),
    )
