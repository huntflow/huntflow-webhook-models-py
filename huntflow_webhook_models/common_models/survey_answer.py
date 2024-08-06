from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field

from huntflow_webhook_models.consts import SurveyAnswerRequestState


class SurveyAnswerRespondent(BaseModel):
    id: int = Field(..., description="Respondent ID", examples=[1])
    account_id: Optional[int] = Field(None, description="Respondent account ID", examples=[1])
    custom_id: Optional[str] = Field(
        None,
        description="Respondent account ID in external system",
        examples=["123"],
    )
    name: str = Field(..., description="Respondent name", examples=["John Doe"])
    email: str = Field(..., description="Respondent email", examples=["test@email.com"])


class SurveyAnswerRequest(BaseModel):
    id: int = Field(..., description="Recruitment evaluation request ID", examples=[1])
    respondent: Optional[SurveyAnswerRespondent] = None
    created: datetime = Field(
        ...,
        description="Date of creation",
        examples=[datetime(1970, 1, 1, 1, 1, 1)],
    )
    state: SurveyAnswerRequestState = Field(..., description="Survey answer request state")


class SurveyAnswerData(BaseModel):
    comment: str = Field(..., description="Survey answer comment", examples=["Great job"])


class SurveyAnswer(BaseModel):
    id: int = Field(..., description="Recruitment evaluation answer ID", examples=[1])
    respondent: SurveyAnswerRespondent = Field(..., description="Respondent")
    created: datetime = Field(
        ...,
        description="Date of creation",
        examples=[datetime(1970, 1, 1, 1, 1, 1)],
    )
    updated: datetime = Field(
        ...,
        description="Update date",
        examples=[datetime(1970, 1, 1, 1, 1, 1)],
    )
    data: SurveyAnswerData = Field(..., description="Additional data")
