from pydantic import BaseModel, Field

from huntflow_webhook_models.base import BaseHuntflowWebhookRequest, WebhookMetaInfoBase
from huntflow_webhook_models.common_models.recruitment_evaluation import RecruitmentEvaluation
from huntflow_webhook_models.consts import CommonWebhookActionType


class RecruitmentEvaluationRequestMeta(WebhookMetaInfoBase):
    webhook_action: CommonWebhookActionType = Field(
        ...,
        description="Webhook action",
        examples=[CommonWebhookActionType.ADD],
    )


class RecruitmentEvaluationEvent(BaseModel):
    recruitment_evaluation: RecruitmentEvaluation


class RecruitmentEvaluationHookRequest(BaseHuntflowWebhookRequest):
    event: RecruitmentEvaluationEvent
    meta: RecruitmentEvaluationRequestMeta
