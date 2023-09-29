from datetime import datetime
from typing import Any, Dict, Optional

from pydantic import BaseModel, Field

from huntflow_webhook_models.consts import ApplicantOfferLogTypes


class AccountApplicantOfferLog(BaseModel):
    id: int = Field(..., description="Log ID", examples=[1])
    type: ApplicantOfferLogTypes = Field(
        ...,
        description="Log type",
        examples=[ApplicantOfferLogTypes.ADD],
    )


class ApplicantOffer(BaseModel):
    id: int = Field(..., description="Offer ID", examples=[1])
    account_applicant_offer_log: AccountApplicantOfferLog = Field(
        ...,
        description="Account applicant offer log",
    )
    applicant_offer_id: int = Field(..., description="Account applicant offer ID", examples=[1])
    created: datetime = Field(
        ...,
        description="Date time the offer was created",
        examples=[datetime(1970, 1, 1, 1, 1, 1)],
    )
    values: Optional[Dict[str, Any]] = Field(
        None,
        description="Additional offer fields",
        examples=[{"position_name": "manager"}],
    )
