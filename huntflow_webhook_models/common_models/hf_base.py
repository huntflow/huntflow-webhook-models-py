from typing import Optional

from pydantic import BaseModel, Field


class AccountFile(BaseModel):
    id: int = Field(..., description="File ID", examples=[1])
    content_type: str = Field(..., description="MIME type", examples=["image/jpeg"])
    name: str = Field(..., description="Filename", examples=["test_file.jpeg"])
    url: str = Field(..., description="File url", examples=["https://domain/file/1"])


class AccountInfo(BaseModel):
    id: int = Field(..., description="Account ID", examples=[1])
    name: str = Field(..., description="Account owner name", examples=["John"])
    email: Optional[str] = Field(
        None,
        description="Account owner email",
        examples=["test@email.com"],
    )


class AccountSource(BaseModel):
    id: int = Field(..., description="Resume source ID", examples=[1])
    foreign: Optional[str] = Field(
        None,
        description="Applicant source foreign",
        examples=["f2"],
    )
    name: str = Field(..., description="Applicant source name", examples=["Headhunter"])
    type: str = Field(..., description="Applicant source type", examples=["user"])
