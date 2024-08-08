from datetime import date, datetime
from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field

from huntflow_webhook_models.common_models.calendar_event import ApplicantLogCalendarEvent
from huntflow_webhook_models.common_models.hf_base import AccountFile, VacancyQuotaItem
from huntflow_webhook_models.common_models.survey_questionary import SurveyQuestionary
from huntflow_webhook_models.common_models.vacancy import Vacancy
from huntflow_webhook_models.consts import AgreementState, ApplicantLogType, SurveyType


class ApplicantSocial(BaseModel):
    id: int = Field(..., description="Social ID", examples=[1])
    social_type: str = Field(..., description="Social type", examples=["TELEGRAM"])
    value: str = Field(..., description="Social nick/email", examples=["test_tg"])
    verified: bool = Field(..., description="Verification flag", examples=[True])
    verification_date: Optional[datetime] = Field(
        None,
        description="Verification datetime",
        examples=[datetime(1970, 1, 1, 1, 1, 1)],
    )


class ApplicantPDAgreement(BaseModel):
    state: Optional[AgreementState] = Field(
        None,
        description="Agreement state",
        examples=[AgreementState.NOT_SENT],
    )
    decision_date: Optional[datetime] = Field(
        None,
        description="Decision date",
        examples=[datetime(1970, 1, 1, 1, 1, 1)],
    )


class VacancyApplicantStatus(BaseModel):
    id: int = Field(..., description="Status ID", examples=[1])
    name: str = Field(..., description="Status name", examples=["hired"])


class ApplicantPhoto(AccountFile):
    pass


class ApplicantExternalAccountSource(BaseModel):
    id: int = Field(..., description="Applicant external account source ID", examples=[1])
    name: Optional[str] = Field(
        ...,
        description="Applicant external account source name",
        examples=["Headhunter"],
    )


class ApplicantExternalAccount(BaseModel):
    id: int = Field(..., description="External ID", examples=[1])
    auth_type: str = Field(..., description="Authentication type", examples=["NATIVE"])
    account_source: Optional[ApplicantExternalAccountSource] = Field(
        None,
        description="Applicant external account source",
    )
    updated: Optional[datetime] = Field(
        None,
        description="Date the applicant external account was modified",
        examples=[datetime(1970, 1, 1, 1, 1, 1)],
    )


class Applicant(BaseModel):
    id: int = Field(..., description="Applicant ID", examples=[1])
    email: Optional[str] = Field(
        None,
        description="Applicant's email",
        examples=["email@example.com"],
    )
    first_name: Optional[str] = Field(
        None,
        description="Applicant's firstname",
        examples=["test_name"],
    )
    last_name: Optional[str] = Field(None, description="Applicant's lastname", examples=["test"])
    middle_name: Optional[str] = Field(
        None,
        description="Applicant's patronymic",
        examples=["test"],
    )
    position: Optional[str] = Field(None, description="Applicant's current job", examples=["test"])
    birthday: Optional[date] = Field(
        None,
        description="Applicant's birthday",
        examples=[date(1970, 1, 1)],
    )
    company: Optional[str] = Field(
        None,
        description="Last company the applicant worked for",
        examples=["test"],
    )
    money: Optional[str] = Field(
        None,
        description="Desired salary of the applicant",
        examples=["10$"],
    )
    phone: Optional[str] = Field(None, description="Applicant's phone", examples=["+99999999"])
    skype: Optional[str] = Field(None, description="Applicant's skype", examples=["test_skype"])
    photo: Optional[ApplicantPhoto] = Field(None, description="Applicant's photo")
    has_photo: bool = Field(..., description="Does the applicant have a photo?", examples=[False])
    social: List[ApplicantSocial] = Field([], description="Applicant social media list")
    questionary: Optional[datetime] = Field(
        None,
        description="Date of filling / changing additional information",
        examples=[datetime(1970, 1, 1, 1, 1, 1, 1)],
    )
    pd_agreement: Optional[ApplicantPDAgreement] = Field(
        None,
        description="Agreement on the processing of personal data",
    )
    values: Optional[Dict[str, Any]] = Field(
        None,
        description="Additional fields",
        examples=[{"favorite_language": "python"}],
    )
    externals: Optional[List[ApplicantExternalAccount]] = None


class Respondent(BaseModel):
    account_id: int = Field(..., description="Account ID", examples=[1])
    custom_id: Optional[int] = Field(None, description="Custom ID", examples=[1])
    name: Optional[str] = Field(None, description="Respondent name", examples=["John"])
    email: str = Field(..., description="Respondent email", examples=["test@example.com"])


class Survey(BaseModel):
    id: int = Field(..., description="Survey ID", examples=[1])
    name: str = Field(..., description="Survey name", examples=["test"])
    type: SurveyType = Field(..., description="Survey type", examples=[SurveyType.TYPE_A])
    created: datetime = Field(
        ...,
        description="Date the survey was created",
        examples=[datetime(1970, 1, 1, 1, 1, 1)],
    )
    updated: Optional[datetime] = Field(
        None,
        description="Date the survey was changed",
        examples=[datetime(1970, 1, 1, 1, 1, 1)],
    )
    active: bool = Field(..., description="Active flag", examples=[True])


class SurveyAnswerOfTypeA(BaseModel):
    id: int = Field(..., description="Survey answer ID", examples=[1])
    respondent: Respondent = Field(..., description="Survey respondent data")
    survey: Survey = Field(..., description="Survey data")
    created: datetime = Field(
        ...,
        description="Date of the questionnaire",
        examples=[datetime(1970, 1, 1, 1, 1, 1)],
    )
    updated: Optional[datetime] = Field(
        None,
        description="Date the questionnaire was modified",
        examples=[datetime(1970, 1, 1, 1, 1, 1)],
    )
    values: Optional[Dict[str, Any]] = Field(
        None,
        description="Survey results",
        examples=[{"question": "answer"}],
    )


class RejectionReason(BaseModel):
    id: int = Field(..., description="Rejection reason ID", examples=[1])
    name: str = Field(..., description="Rejection reason name", examples=["Too far"])


class ApplicantLog(BaseModel):
    id: int = Field(..., description="Applicant log ID", examples=[1])
    type: ApplicantLogType = Field(
        ...,
        description="Applicant log type",
        examples=[ApplicantLogType.STATUS],
    )
    status: Optional[VacancyApplicantStatus] = None
    employment_date: Optional[date] = Field(
        None,
        description="Employment date",
        examples=[date(1970, 1, 1)],
    )
    removed: Optional[datetime] = Field(
        None,
        description="Record delete date time",
        examples=[datetime(1970, 1, 1, 1, 1, 1)],
    )
    comment: Optional[str] = Field(None, description="Comment", examples=["comment"])
    created: datetime = Field(
        ...,
        description="Log creation date time",
        examples=[datetime(1970, 1, 1, 1, 1, 1)],
    )
    source: Optional[str] = None
    files: List[AccountFile] = Field([], description="List of uploaded files")
    survey_answer_of_type_a: Optional[SurveyAnswerOfTypeA] = Field(
        None,
        description="Survey questionary data",
    )
    rejection_reason: Optional[RejectionReason] = Field(
        None,
        description="Rejection reason data",
    )
    survey_questionary: Optional[SurveyQuestionary] = Field(
        None,
        description="Survey questionary data",
    )
    calendar_event: Optional[ApplicantLogCalendarEvent] = Field(
        None,
        description="Calendar event data",
    )
    vacancy: Optional[Vacancy] = Field(None, description="Vacancy data")
    hired_in_fill_quota: Optional[VacancyQuotaItem] = Field(
        None,
        description="Quota data by which applicant was hired",
    )


class ApplicantTag(BaseModel):
    id: int = Field(..., description="Tag ID", examples=[1])
    name: str = Field(..., description="Tag name", examples=["COOL"])
    color: str = Field(..., description="Tag color", examples=["000000"])
