from pydantic import BaseModel

from huntflow_webhook_models.base import BaseHuntflowWebhookRequest, WebhookMetaInfoBase
from huntflow_webhook_models.common_models.recruitment_evaluation import RecruitmentEvaluation
from huntflow_webhook_models.consts import CommonWebhookActionType


class RecruitmentEvaluationRequestMeta(WebhookMetaInfoBase):
    webhook_action: CommonWebhookActionType


class RecruitmentEvaluationEvent(BaseModel):
    recruitment_evaluation: RecruitmentEvaluation


class RecruitmentEvaluationHookRequest(BaseHuntflowWebhookRequest):
    event: RecruitmentEvaluationEvent
    meta: RecruitmentEvaluationRequestMeta
