from pydantic import BaseModel, Field

from huntflow_webhook_models.base import BaseHuntflowWebhookRequest, WebhookMetaInfoBase
from huntflow_webhook_models.common_models.applicant import Applicant
from huntflow_webhook_models.common_models.applicant_offer import ApplicantOffer
from huntflow_webhook_models.common_models.vacancy import Vacancy
from huntflow_webhook_models.consts import CommonWebhookActionType


class OfferHookRequestMeta(WebhookMetaInfoBase):
    webhook_action: CommonWebhookActionType = Field(
        ...,
        description="Webhook action",
        examples=[CommonWebhookActionType.ADD],
    )


class OfferEvent(BaseModel):
    vacancy: Vacancy
    applicant: Applicant
    applicant_offer: ApplicantOffer


class OfferHookRequest(BaseHuntflowWebhookRequest):
    event: OfferEvent
    meta: OfferHookRequestMeta
