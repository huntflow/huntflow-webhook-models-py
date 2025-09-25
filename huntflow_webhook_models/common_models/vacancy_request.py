import datetime
from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field

from huntflow_webhook_models.common_models.hf_base import AccountInfo, File
from huntflow_webhook_models.consts import VacancyRequestLogAction, VacancyRequestStatus


class VacancyRequestApprovalState(BaseModel):
    id: int = Field(..., description="Approval ID")

    status: VacancyRequestStatus = Field(..., description="Approval status")
    email: str = Field(
        ...,
        description="Email, which was used to send the request for approval",
    )
    reason: Optional[str] = Field(
        None,
        description="Rejection reason",
    )
    order: Optional[int] = Field(None, description="Approval order number")
    changed: Optional[datetime.datetime] = Field(
        None,
        description="Date and time of the last approval change",
    )


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
    account: int = Field(..., description="Account ID")
    vacancy: int = Field(..., description="Vacancy ID")
    updated: Optional[datetime.datetime] = Field(
        None,
        description="Date and time of editing of the request",
        examples=[datetime.datetime(1970, 1, 1, 1, 1, 1)],
    )
    changed: Optional[datetime.datetime] = Field(
        None,
        description="Date and time of attaching to vacancy",
        examples=[datetime.datetime(1970, 1, 1, 1, 1, 1)],
    )
    states: List[VacancyRequestApprovalState] = Field([], description="List of approval states")
    account_info: Optional[AccountInfo]
    status: Optional[VacancyRequestStatus] = Field(..., description="Vacancy request status")
    files: List[File] = Field([], description="List of uploaded files")


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
