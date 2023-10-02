from typing import Any, Dict, List

from pydantic import BaseModel, Field


class SurveySchema(BaseModel):
    type: str = Field(
        ...,
        description="Recruitment evaluation survey schema type",
        examples=["object"],
    )
    required: List[str] = Field(
        ...,
        description="Recruitment evaluation survey schema required fields",
        examples=[["stars", "comment"]],
    )
    properties: Dict[str, Any] = Field(
        ...,
        description="Recruitment evaluation survey schema fields description",
    )
    additionalProperties: bool = Field(
        ...,
        description="Permission to add fields not specified in properties in response to a survey. "
        "Always false",
        examples=[False],
    )


class AccountSurvey(BaseModel):
    id: int = Field(..., description="Recruitment evaluation survey ID", examples=[1])
    name: str = Field(
        ...,
        description="Recruitment evaluation survey name ",
        examples=["Recruitment evaluation"],
    )
    schema_: SurveySchema = Field(
        ...,
        description="Recruitment evaluation survey schema",
        alias="schema",
    )
