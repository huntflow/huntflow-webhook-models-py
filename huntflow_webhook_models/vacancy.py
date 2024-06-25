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


class VacancyEvent(BaseModel):
    vacancy: Vacancy
    vacancy_log: VacancyLog


class VacancyHookRequest(BaseHuntflowWebhookRequest):
    event: VacancyEvent
    meta: VacancyHookRequestMeta
