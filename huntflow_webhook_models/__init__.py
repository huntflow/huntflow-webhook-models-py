from pydantic import BaseModel, ConfigDict

from . import consts
from .applicant import ApplicantHookRequest
from .offer import OfferHookRequest
from .recruitment_evaluation import RecruitmentEvaluationHookRequest
from .response import ResponseHookRequest
from .survey_questionary import SurveyQuestionaryHookRequest
from .vacancy import VacancyHookRequest
from .vacancy_request import VacancyRequestHookRequest

BaseModel.model_config = ConfigDict(extra="forbid")

__all__ = [
    "consts",
    "ApplicantHookRequest",
    "VacancyHookRequest",
    "VacancyRequestHookRequest",
    "OfferHookRequest",
    "RecruitmentEvaluationHookRequest",
    "ResponseHookRequest",
    "SurveyQuestionaryHookRequest",
]
