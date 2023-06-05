from datetime import date, datetime
from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field

from huntflow_webhook_models.common_models.calendar_event import ApplicantLogCalendarEvent
from huntflow_webhook_models.common_models.hf_base import AccountFile
from huntflow_webhook_models.common_models.survey_questionary import SurveyQuestionary
from huntflow_webhook_models.common_models.vacancy import Vacancy
from huntflow_webhook_models.consts import AgreementState, ApplicantLogType, SurveyType


class ApplicantSocial(BaseModel):
    id: int = Field(..., description="Social ID", example=1)
    social_type: str = Field(..., description="Social type", example="TELEGRAM")
    value: str = Field(..., description="Social nick/email", example="test_tg")
    verified: bool = Field(..., description="Verification flag", example=True)
    verification_date: Optional[datetime] = Field(
        None,
        description="Verification datetime",
        example=datetime(1970, 1, 1, 1, 1, 1),
    )


class ApplicantPDAgreement(BaseModel):
    state: Optional[AgreementState] = Field(
        None,
        description="Agreement state",
        example=AgreementState.NOT_SENT,
    )
    decision_date: Optional[datetime] = Field(
        None,
        description="Decision date",
        example=datetime(1970, 1, 1, 1, 1, 1),
    )


class VacancyApplicantStatus(BaseModel):
    id: int = Field(..., description="Status ID", example=1)
    name: str = Field(..., description="Status name", example="hired")


class ApplicantPhoto(AccountFile):
    pass


class Applicant(BaseModel):
    id: int = Field(..., description="Applicant ID", example=1)
    email: Optional[str] = Field(None, description="Applicant's email", example="email@example.com")
    first_name: str = Field(..., description="Applicant's firstname", example="test_name")
    last_name: str = Field(..., description="Applicant's lastname", example="test")
    middle_name: Optional[str] = Field(None, description="Applicant's patronymic", example="test")
    position: Optional[str] = Field(None, description="Applicant's current job", example="test")
    birthday: Optional[date] = Field(
        None,
        description="Applicant's birthday",
        example=date(1970, 1, 1),
    )
    company: Optional[str] = Field(
        None,
        description="Last company the applicant worked for",
        example="test",
    )
    money: Optional[str] = Field(None, description="Desired salary of the applicant", example="10$")
    phone: Optional[str] = Field(None, description="Applicant's phone", example="+99999999")
    skype: Optional[str] = Field(None, description="Applicant's skype", example="test_skype")
    photo: Optional[ApplicantPhoto] = Field(None, description="Applicant's photo")
    social: List[ApplicantSocial] = Field([], description="Applicant social media list")
    questionary: Optional[datetime] = Field(
        None,
        description="Date of filling / changing additional information",
        example=datetime(1970, 1, 1, 1, 1, 1, 1),
    )
    pd_agreement: Optional[ApplicantPDAgreement] = Field(
        None,
        description="Agreement on the processing of personal data",
    )
    values: Optional[Dict[str, Any]] = Field(
        None,
        description="Additional applicant fields",
        example={"favorite_language": "python"},
    )


class Respondent(BaseModel):
    account_id: int = Field(..., description="Account ID", example=1)
    custom_id: int = Field(..., description="Custom ID", example=1)
    name: Optional[str] = Field(None, description="Respondent name", example="John")
    email: str = Field(..., description="Respondent email", example="test@example.com")


class Survey(BaseModel):
    id: int = Field(..., description="Survey ID", example=1)
    name: str = Field(..., description="Survey name", example="test")
    type: SurveyType = Field(..., description="Survey type", example=SurveyType.TYPE_A)
    created: datetime = Field(
        ...,
        description="Date the survey was created",
        example=datetime(1970, 1, 1, 1, 1, 1),
    )
    updated: Optional[datetime] = Field(
        None,
        description="Date the survey was changed",
        example=datetime(1970, 1, 1, 1, 1, 1),
    )
    active: bool = Field(..., description="Active flag", example=True)


class SurveyAnswerOfTypeA(BaseModel):
    id: int = Field(..., description="Survey answer ID", example=1)
    respondent: Respondent
    survey: Survey
    created: datetime = Field(
        ...,
        description="Date of the questionnaire",
        example=datetime(1970, 1, 1, 1, 1, 1),
    )
    updated: Optional[datetime] = Field(
        ...,
        description="Date the questionnaire was modified",
        example=datetime(1970, 1, 1, 1, 1, 1),
    )
    values: Optional[Dict[str, Any]] = Field(
        None,
        description="Survey results",
        example={"question": "answer"},
    )


class RejectionReason(BaseModel):
    id: int = Field(..., description="Rejection reason ID", example=1)
    name: str = Field(..., description="Rejection reason name", example="Too far")


class ApplicantLog(BaseModel):
    id: int = Field(..., description="Applicant log ID", example=1)
    type: ApplicantLogType = Field(
        ...,
        description="Applicant log type",
        example=ApplicantLogType.STATUS,
    )
    status: Optional[VacancyApplicantStatus] = None
    employment_date: Optional[date] = Field(
        None,
        description="Applicant employment date",
        example=date(1970, 1, 1),
    )
    removed: Optional[datetime] = Field(
        None,
        description="Record delete date time",
        example=datetime(1970, 1, 1, 1, 1, 1),
    )
    comment: Optional[str] = Field(None, description="Comment", example="comment")
    created: datetime = Field(
        ...,
        description="Log creation date time",
        example=datetime(1970, 1, 1, 1, 1, 1),
    )
    source: Optional[str]
    files: List[AccountFile] = Field([], description="List of uploaded files")
    survey_answer_of_type_a: Optional[SurveyAnswerOfTypeA] = None
    rejection_reason: Optional[RejectionReason] = None
    survey_questionary: Optional[SurveyQuestionary] = None
    calendar_event: Optional[ApplicantLogCalendarEvent] = None
    vacancy: Optional[Vacancy] = None


class ApplicantTag(BaseModel):
    id: int = Field(..., description="Tag ID", example=1)
    name: str = Field(..., description="Tag name", example="COOL")
    color: str = Field(..., description="Tag color", example="000000")
