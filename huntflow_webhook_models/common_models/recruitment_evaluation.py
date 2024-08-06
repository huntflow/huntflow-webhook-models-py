from typing import List, Optional

from pydantic import BaseModel, Field

from huntflow_webhook_models.common_models.account_survey import AccountSurvey
from huntflow_webhook_models.common_models.applicant import Applicant
from huntflow_webhook_models.common_models.survey_answer import SurveyAnswer, SurveyAnswerRequest
from huntflow_webhook_models.common_models.vacancy import Vacancy


class RecruitmentEvaluation(BaseModel):
    id: int = Field(..., description="Recruitment evaluation ID", examples=[1])
    account_survey: AccountSurvey = Field(
        ...,
        description="Recruitment evaluation survey data",
    )
    survey_answer_requests: List[SurveyAnswerRequest] = Field(
        [],
        description="List of recruitment evaluation requests",
    )
    survey_answer: Optional[SurveyAnswer] = Field(
        None,
        description="Response to recruitment evaluation request",
    )
    stars: Optional[int] = Field(None, description="Evaluation level", examples=[10])
    applicant: Applicant = Field(..., description="Applicant data")
    vacancy: Vacancy = Field(..., description="Vacancy data")
    applicant_log_id: int = Field(..., description="Applicant log ID")
