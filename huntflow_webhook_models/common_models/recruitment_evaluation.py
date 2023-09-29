from typing import List, Optional

from pydantic import BaseModel, Field

from huntflow_webhook_models.common_models.account_survey import AccountSurvey
from huntflow_webhook_models.common_models.applicant import Applicant
from huntflow_webhook_models.common_models.survey_answer import SurveyAnswer, SurveyAnswerRequest
from huntflow_webhook_models.common_models.vacancy import Vacancy


class RecruitmentEvaluation(BaseModel):
    id: int = Field(..., description="Recruitment evaluation ID", examples=[1])
    account_survey: AccountSurvey
    survey_answer_requests: List[SurveyAnswerRequest]
    survey_answer: Optional[SurveyAnswer] = Field(
        None,
        description="Response to recruitment evaluation request",
    )
    stars: Optional[int] = Field(None, description="Evaluation level", examples=[10])
    applicant: Applicant
    vacancy: Vacancy