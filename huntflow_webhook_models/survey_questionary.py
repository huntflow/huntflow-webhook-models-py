from pydantic import BaseModel, Field

from huntflow_webhook_models.base import BaseHuntflowWebhookRequest, WebhookMetaInfoBase
from huntflow_webhook_models.common_models.applicant import Applicant
from huntflow_webhook_models.common_models.response import VacancyExternal
from huntflow_webhook_models.common_models.survey_questionary import SurveyQuestionary
from huntflow_webhook_models.consts import CommonWebhookActionType


class SurveyQuestionaryHookRequestMeta(WebhookMetaInfoBase):
    webhook_action: CommonWebhookActionType = Field(
        ...,
        description="Webhook action",
        examples=[CommonWebhookActionType.ADD],
    )


class SurveyQuestionaryEvent(BaseModel):
    applicant: Applicant
    vacancy: VacancyExternal
    applicant_log_id: int = Field(..., description="Applicant log ID", examples=[1])
    survey_questionary: SurveyQuestionary


class SurveyQuestionaryHookRequest(BaseHuntflowWebhookRequest):
    event: SurveyQuestionaryEvent
    meta: SurveyQuestionaryHookRequestMeta
