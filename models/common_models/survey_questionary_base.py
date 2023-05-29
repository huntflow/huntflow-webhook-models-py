from datetime import datetime
from typing import Dict, Optional

from pydantic import BaseModel, Field


class Survey(BaseModel):
    __survey_schema_example = {
        "type": "object",
        "required": ["d4hm5pRsbXPEQUSyiqXJA"],
        "properties": {
            "d4hm5pRsbXPEQUSyiqXJA": {
                "type": "string",
                "title": "Hard question",
                "minLength": 3,
                "isNotEmpty": True,
            },
        },
        "additionalProperties": False,
    }
    __ui_schema_example = {
        "ui:order": ["d4hm5pRsbXPEQUSyiqXJA"],
        "d4hm5pRsbXPEQUSyiqXJA": {
            "ui:widget": "TextWidget",
            "ui:description": "Hard question",
            "ui:placeholder": "answer here",
        },
    }
    id: int = Field(..., description="Survey ID", example=1)
    name: str = Field(..., description="Survey name", example="test")
    schema_: Dict[str, str] = Field(
        ...,
        alias="schema",
        description="Survey schema",
        example=__survey_schema_example,
    )
    ui_schema: Dict[str, str] = Field(
        ...,
        description="UI schema",
        example=__ui_schema_example,
    )
    created: datetime = Field(
        ...,
        description="Date time the survey was created",
        example=datetime(1970, 1, 1, 1, 1, 1),
    )
    updated: Optional[datetime] = Field(
        ...,
        description="Date time the survey was updated",
        example=datetime(1970, 1, 1, 1, 1, 1),
    )
    title: str = Field(..., description="Survey title", example="Test")
    active: bool = Field(..., description="Active flag", example=False)
    type: str = Field("type_q", description="Survey type (always type_q)")


class Respondent(BaseModel):
    applicant_id: int = Field(..., description="Applicant ID", example=1)
    name: str = Field(..., description="Applciant name", example="John")


class CreatedBy(BaseModel):
    account_id: int = Field(..., description="Account ID", example=1)
    name: str = Field(..., description="Creator name", example="John")


class Answer(BaseModel):
    id: int = Field(..., description="Answer ID", example=1)
    created: datetime = Field(
        ...,
        description="Answer date time",
        example=datetime(1970, 1, 1, 1, 1, 1),
    )
    data: Dict[str, str] = Field(
        {},
        description="Answer data",
        example={"d4hm5pRsbXPEQUSyiqXJA": "Applicant's smart answer"},
    )


class SurveyQuestionary(BaseModel):
    id: int = Field(..., description="Survey questionary ID", example=1)
    survey: Survey
    created: datetime = Field(
        ...,
        description="Date time the survey questionary was created",
        example=datetime(1970, 1, 1, 1, 1, 1),
    )
    respondent: Respondent
    created_by: CreatedBy
    answer: Answer
    link: str = Field(
        ...,
        description="Survey link",
        example="https://survey-questionary/link",
    )
