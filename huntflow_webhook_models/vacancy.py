from pydantic import BaseModel

from huntflow_webhook_models.base import BaseHuntflowWebhookRequest, WebhookMetaInfoBase
from huntflow_webhook_models.common_models.vacancy import Vacancy, VacancyLog
from huntflow_webhook_models.consts import CommonWebhookActionType


class VacancyHookRequestMeta(WebhookMetaInfoBase):
    webhook_action: CommonWebhookActionType


class VacancyEvent(BaseModel):
    vacancy: Vacancy
    vacancy_log: VacancyLog


class VacancyHookRequest(BaseHuntflowWebhookRequest):
    event: VacancyEvent
    meta: VacancyHookRequestMeta
