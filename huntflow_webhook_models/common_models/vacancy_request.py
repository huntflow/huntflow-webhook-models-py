import datetime
from typing import Any, Dict, Optional

from pydantic import BaseModel, Field

from huntflow_webhook_models.consts import VacancyRequestLogAction


class VacancyRequest(BaseModel):
    id: int = Field(..., description="Vacancy request ID", examples=[1])
    account_vacancy_request: int = Field(
        ...,
        description="Account vacancy request ID",
        examples=[1],
    )
    created: datetime.datetime = Field(
        ...,
        description="Date time vacancy request created",
        examples=[datetime.datetime(1970, 1, 1, 1, 1, 1)],
    )
    position: str = Field(..., description="Vacancy position", examples=["Developer"])
    values: Dict[str, Any] = Field(
        ...,
        description="Vacancy request fields",
        examples=[{"company": "test_company"}],
    )


class VacancyRequestLog(BaseModel):
    id: int = Field(..., description="Vacancy request log ID", examples=[1])
    action: VacancyRequestLogAction = Field(
        ...,
        description="Vacancy request log action",
        examples=[VacancyRequestLogAction.CREATE],
    )
    created: datetime.datetime = Field(
        ...,
        description="Date time vacancy request log created",
        examples=[datetime.datetime(1970, 1, 1, 1, 1, 1)],
    )
    reason: Optional[str] = Field(
        None,
        description="Vacancy close/hold reason",
        examples=["All hired"],
    )
