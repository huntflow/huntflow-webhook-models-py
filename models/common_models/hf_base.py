from typing import Optional

from pydantic import BaseModel, Field


class AccountFile(BaseModel):
    id: int = Field(..., description="File ID", exmple=1)
    content_type: str = Field(..., description="MIME type", example="image/jpeg")
    name: str = Field(..., description="Filename", example="test_file.jpeg")
    url: str = Field(..., description="File url", example="https://domain/file/1")


class AccountInfo(BaseModel):
    id: int = Field(..., description="Account ID", example=1)
    name: str = Field(..., description="Account owner name", example="John")
    email: Optional[str] = Field(..., description="Account owner email", example="test@email.com")
