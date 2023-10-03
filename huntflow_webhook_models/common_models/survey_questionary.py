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
    id: int = Field(..., description="Survey ID", examples=[1])
    name: str = Field(..., description="Survey name", examples=["test"])
    schema_: Dict[str, str] = Field(
        ...,
        alias="schema",
        description="Survey schema",
        examples=[__survey_schema_example],
    )
    ui_schema: Dict[str, str] = Field(
        ...,
        description="UI schema",
        examples=[__ui_schema_example],
    )
    created: datetime = Field(
        ...,
        description="Date time the survey was created",
        examples=[datetime(1970, 1, 1, 1, 1, 1)],
    )
    updated: Optional[datetime] = Field(
        None,
        description="Date time the survey was updated",
        examples=[datetime(1970, 1, 1, 1, 1, 1)],
    )
    title: str = Field(..., description="Survey title", examples=["Test"])
    active: bool = Field(..., description="Active flag", examples=[False])
    type: str = Field("type_q", description="Survey type (always type_q)", examples=["type_q"])


class Respondent(BaseModel):
    applicant_id: int = Field(..., description="Applicant ID", examples=[1])
    name: str = Field(..., description="Applicant name", examples=["John"])


class CreatedBy(BaseModel):
    account_id: int = Field(..., description="Account ID", examples=[1])
    name: str = Field(..., description="Creator name", examples=["John"])


class Answer(BaseModel):
    id: int = Field(..., description="Answer ID", examples=[1])
    created: datetime = Field(
        ...,
        description="Answer date time",
        examples=[datetime(1970, 1, 1, 1, 1, 1)],
    )
    data: Dict[str, str] = Field(
        {},
        description="Answer data",
        examples=[{"d4hm5pRsbXPEQUSyiqXJA": "Applicant's smart answer"}],
    )


class SurveyQuestionary(BaseModel):
    id: int = Field(..., description="Survey questionary ID", examples=[1])
    survey: Survey
    created: datetime = Field(
        ...,
        description="Date time the survey questionary was created",
        examples=[datetime(1970, 1, 1, 1, 1, 1)],
    )
    respondent: Respondent
    created_by: CreatedBy
    answer: Answer
    link: str = Field(
        ...,
        description="Survey link",
        examples=["https://survey-questionary/link"],
    )
