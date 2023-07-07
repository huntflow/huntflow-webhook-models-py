from pydantic import BaseModel

from huntflow_webhook_models.base import BaseHuntflowWebhookRequest, WebhookMetaInfoBase
from huntflow_webhook_models.common_models.response import (
    ApplicantExternalResponse,
    VacancyExternal,
)
from huntflow_webhook_models.consts import CommonWebhookActionType


class ResponseHookRequestMeta(WebhookMetaInfoBase):
    webhook_action: CommonWebhookActionType


class ResponseEvent(BaseModel):
    applicant_external_response: ApplicantExternalResponse
    vacancy_external: VacancyExternal


class ResponseHookRequest(BaseHuntflowWebhookRequest):
    event: ResponseEvent
    meta: ResponseHookRequestMeta
