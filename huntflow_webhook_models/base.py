from typing import Dict, Optional

from pydantic import BaseModel, Field

from huntflow_webhook_models.consts import WebhookEventType


class Account(BaseModel):
    id: int = Field(..., description="Account ID", examples=[1])
    name: str = Field(..., description="Account name", examples=["Huntflow"])
    nick: str = Field(..., description="Account nick", examples=["HF"])


class Author(BaseModel):
    id: int = Field(..., description="Account ID", examples=[1])
    email: str = Field(..., description="Account owner email", examples=["test@example.com"])
    name: str = Field(..., description="Account owner name", examples=["John"])
    meta: Optional[Dict] = Field(None, description="Additional data", examples=[{"data": "data"}])


class WebhookMetaInfoBase(BaseModel):
    account: Account
    author: Optional[Author] = None
    event_type: WebhookEventType = Field(
        ...,
        description="Webhook event type",
        examples=[WebhookEventType.APPLICANT],
    )
    version: str = Field(..., description="Webhook version", examples=["2.0"])
    retry: int = Field(..., description="Webhook retry count", examples=[1])
    event_id: str = Field(..., description="Event ID", examples=["1"])
    domain: str = Field(..., description="Domain", examples=["huntflow.ai"])


class BaseHuntflowWebhookRequest(BaseModel):
    changes: Optional[Dict] = Field(None, description="Data changes", examples=[{"id": 2}])
    meta: WebhookMetaInfoBase
