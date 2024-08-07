from typing import Optional

from pydantic import BaseModel, Field

from huntflow_webhook_models.base import BaseHuntflowWebhookRequest, WebhookMetaInfoBase
from huntflow_webhook_models.common_models.vacancy import Vacancy, VacancyLog
from huntflow_webhook_models.consts import CommonWebhookActionType


class VacancyHookRequestMeta(WebhookMetaInfoBase):
    webhook_action: CommonWebhookActionType = Field(
        ...,
        description="Webhook action",
        examples=[CommonWebhookActionType.ADD],
    )


class User(BaseModel):
    id: int = Field(..., description="User ID", examples=[1])
    name: str = Field(..., description="User name", examples=["user@example.com"])


class VacancyEvent(BaseModel):
    vacancy: Vacancy
    vacancy_log: VacancyLog
    user: Optional[User] = Field(None, description="Recruiter who joined or left a vacancy")


class VacancyHookRequest(BaseHuntflowWebhookRequest):
    event: VacancyEvent
    meta: VacancyHookRequestMeta
