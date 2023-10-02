from pydantic import BaseModel

from huntflow_webhook_models.base import BaseHuntflowWebhookRequest, WebhookMetaInfoBase
from huntflow_webhook_models.common_models.applicant import Applicant
from huntflow_webhook_models.common_models.response import VacancyExternal
from huntflow_webhook_models.common_models.survey_questionary import SurveyQuestionary
from huntflow_webhook_models.consts import CommonWebhookActionType


class SurveyQuestionaryHookRequestMeta(WebhookMetaInfoBase):
    webhook_action: CommonWebhookActionType


class SurveyQuestionaryEvent(BaseModel):
    applicant: Applicant
    vacancy: VacancyExternal
    applicant_log_id: int
    survey_questionary: SurveyQuestionary


class SurveyQuestionaryHookRequest(BaseHuntflowWebhookRequest):
    event: SurveyQuestionaryEvent
    meta: SurveyQuestionaryHookRequestMeta
