from typing import Dict, Optional

from pydantic import BaseModel, Field

from models.consts import WebhookEventType


class Account(BaseModel):
    id: int = Field(..., description="Account ID", example=1)
    name: str = Field(..., description="Account name", example="Huntflow")
    nick: str = Field(..., description="Account nick", example="HF")


class Author(BaseModel):
    id: int = Field(..., description="Account ID", example=1)
    email: str = Field(..., description="Account owner email", example="test@example.com")
    name: str = Field(..., description="Account owner name", example="John")
    meta: Optional[Dict] = Field(None, description="Additional data", example={"data": "data"})


class WebhookMetaInfoBase(BaseModel):
    account: Account
    author: Author
    event_type: WebhookEventType = Field(
        ...,
        description="Webhook event type",
        example=WebhookEventType.APPLICANT,
    )
    version: str = Field(..., description="Webhook version", example="2.0")
    retry: int = Field(..., description="Webhook retry count", example=1)
    event_id: str = Field(..., description="Event ID", example="1")


class BaseHuntflowWebhookRequest(BaseModel):
    changes: Optional[Dict] = Field(..., description="Data changes", example={"id": 2})
    meta: WebhookMetaInfoBase
