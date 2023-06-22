from pydantic import BaseModel

from huntflow_webhook_models.base import BaseHuntflowWebhookRequest, WebhookMetaInfoBase
from huntflow_webhook_models.common_models.vacancy_request import VacancyRequest, VacancyRequestLog
from huntflow_webhook_models.consts import CommonWebhookActionType


class VacancyRequestHookRequestMeta(WebhookMetaInfoBase):
    webhook_action: CommonWebhookActionType


class VacancyRequestEvent(BaseModel):
    vacancy_request: VacancyRequest
    vacancy_request_log: VacancyRequestLog


class VacancyRequestHookRequest(BaseHuntflowWebhookRequest):
    event: VacancyRequestEvent
    meta: VacancyRequestHookRequestMeta
