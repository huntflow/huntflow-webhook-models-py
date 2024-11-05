from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, Field

from huntflow_webhook_models.consts import (
    CalendarEventReminderMethod,
    CalendarEventState,
    CalendarEventStatus,
    CalendarEventType,
    Transparency,
)


class CalendarEventCreator(BaseModel):
    displayName: Optional[str] = Field(
        None,
        description="Event creator name",
        examples=["John"],
    )
    email: str = Field(..., description="Event creator email", examples=["test@email.com"])
    self: Optional[bool] = Field(
        False,
        description="Flag indicating that you are the creator of the event",
        examples=[False],
    )


class CalendarEventAttendee(BaseModel):
    contact_id: Optional[int] = Field(None, description="Attendee contact ID", examples=[1])
    displayName: Optional[str] = Field(None, description="Attendee display name", examples=["John"])
    email: Optional[str] = Field(None, description="Attendee email", examples=["test@email.com"])
    member: Optional[int] = Field(None, description="Coworker ID", examples=[1])
    name: Optional[str] = Field(None, description="Attendee name", examples=["John"])
    order: Optional[int] = Field(None, description="Attendee order", examples=[1])
    resource: bool = Field(..., description="Attendee resource flag", examples=[False])
    responseStatus: Optional[CalendarEventStatus] = Field(
        None,
        description="Attendee response status",
        examples=[CalendarEventStatus.accepted],
    )


class Conference(BaseModel):
    id: int = Field(..., description="Conference ID", examples=[1])
    topic: Optional[str] = Field(None, description="Conference topic", examples=["Interview"])
    auth_type: Optional[str] = Field(None, description="Conference venue", examples=["ZOOM"])
    state: Optional[str] = Field(
        None,
    )
    start_time: Optional[datetime] = Field(
        None,
        description="Conference start",
        examples=[datetime(1970, 1, 1, 1, 1, 1)],
    )
    end_time: Optional[datetime] = Field(
        None,
        description="Conference end",
        examples=[datetime(1970, 1, 1, 1, 1, 1)],
    )
    timezone: Optional[str] = Field(
        None,
        description="Conference timezone",
        examples=["Africa/Accra"],
    )
    created: datetime = Field(
        ...,
        description="Conference creation datetime",
        examples=[datetime(1970, 1, 1, 1, 1, 1)],
    )
    changed: Optional[datetime] = Field(
        None,
        description="Conference change datetime",
        examples=[datetime(1970, 1, 1, 1, 1, 1)],
    )
    foreign: Optional[str] = Field(
        None,
        description="Foreign conference ID",
        examples=["conference_id"],
    )
    link: Optional[str] = Field(
        None,
        description="Conference link",
        examples=["https://conference/link"],
    )
    access_code: Optional[str] = Field(
        None,
        description="Conference access code",
        examples=["conference_code"],
    )


class CalendarEventReminder(BaseModel):
    method: CalendarEventReminderMethod = Field(
        ...,
        description="Reminder method",
        examples=[CalendarEventReminderMethod.popup],
    )
    minutes: int = Field(
        ...,
        description="How many minutes in advance to remind about the event",
        examples=[1],
    )
    multiplier: str = Field(
        ...,
        description="Reminder unit of measure.",
        examples=["minutes"],
    )
    value: int = Field(
        ...,
        description="How many units in advance to remind about the event in multiplier",
        examples=[1],
    )


class InterviewType(BaseModel):
    id: int = Field(..., description="Interview type ID", examples=[1])
    name: str = Field(..., description="Interview type name", examples=["Phone Interview"])


class ApplicantLogCalendarEvent(BaseModel):
    id: int = Field(..., description="Calendar event ID", examples=[1])
    name: Optional[str] = Field(None, description="Event name", examples=["Test Name"])
    description: Optional[str] = Field(
        None,
        description="Event description",
        examples=["Interview with John Doe"],
    )
    status: CalendarEventStatus = Field(
        ...,
        description="Event status",
        examples=[CalendarEventStatus.accepted],
    )
    event_type: CalendarEventType = Field(
        ...,
        description="Event type",
        examples=[CalendarEventType.interview],
    )
    interview_type: Optional[InterviewType] = Field(None, description="Interview type")
    start: datetime = Field(
        ...,
        description="Event start date and time",
        examples=[datetime(1970, 1, 1, 1, 1, 1)],
    )
    end: datetime = Field(
        ...,
        description="Event end date and time",
        examples=[datetime(1970, 1, 1, 1, 1, 1)],
    )
    timezone: Optional[str] = Field(None, description="Event time zone", examples=["Africa/Accra"])
    attendees: List[CalendarEventAttendee] = Field(
        [],
        description="Event attendees (participants)",
    )
    created: datetime = Field(
        ...,
        description="Date and time of event creation",
        examples=[datetime(1970, 1, 1, 1, 1, 1)],
    )
    creator: Optional[CalendarEventCreator] = Field(None, description="Event creator")
    reminders: List[CalendarEventReminder] = Field(
        [],
        description="List of reminders",
    )
    all_day: bool = Field(
        ...,
        description="Flag indicating that the event is scheduled for the whole day",
        examples=[False],
    )
    foreign: Optional[str] = Field(None, description="Foreign event ID", examples=["f1"])
    recurrence: Optional[List] = None
    etag: Optional[str] = Field(None, description="Event Etag", examples=[1633413621888])
    location: Optional[str] = Field(None, description="Event location", examples=["Some location"])
    transparency: Transparency = Field(
        ...,
        description="Event transparency (availability)",
        examples=[Transparency.busy],
    )
    conference: Optional[Conference] = Field(None, description="Event conference data")
    state: Optional[CalendarEventState] = Field(
        None,
        description="Event state",
        examples=[CalendarEventState.QUEUED],
    )
