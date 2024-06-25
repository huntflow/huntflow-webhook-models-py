from typing import List

from pydantic import BaseModel, Field

from huntflow_webhook_models.base import BaseHuntflowWebhookRequest, WebhookMetaInfoBase
from huntflow_webhook_models.common_models.applicant import Applicant, ApplicantLog, ApplicantTag
from huntflow_webhook_models.consts import ApplicantWebhookActionType


class ApplicantEvent(BaseModel):
    applicant: Applicant
    applicant_log: ApplicantLog
    applicant_tags: List[ApplicantTag]


class ApplicantHookRequestMeta(WebhookMetaInfoBase):
    webhook_action: ApplicantWebhookActionType = Field(
        ...,
        description="Webhook action",
        examples=[ApplicantWebhookActionType.ADD],
    )


class ApplicantHookRequest(BaseHuntflowWebhookRequest):
    event: ApplicantEvent
    meta: ApplicantHookRequestMeta
