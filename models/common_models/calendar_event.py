from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, Field

from models.consts import (
    CalendarEventReminderMethod,
    CalendarEventStatus,
    CalendarEventType,
    Transparency,
)


class CalendarEventCreator(BaseModel):
    displayName: Optional[str] = Field(
        None,
        description="Event creator name",
        example="John",
    )
    email: str = Field(..., description="Event creator email", example="test@email.com")
    self: Optional[bool] = Field(
        False,
        description="Flag indicating that you are the creator of the event",
        example=False,
    )


class CalendarEventAttendee(BaseModel):
    contact_id: Optional[int] = Field(None, description="Attendee contact ID", example=1)
    displayName: Optional[str] = Field(None, description="Attendee display name", example="John")
    email: Optional[str] = Field(None, description="Attendee email", example="test@email.com")
    member: Optional[int] = Field(None, description="Coworker ID", example=1)
    name: Optional[str] = Field(None, description="Attendee name", example="John")
    order: Optional[int] = Field(None, description="Attendee order", example=1)
    resource: bool = Field(..., description="Attendee resource flag", example=False)
    responseStatus: Optional[CalendarEventStatus] = Field(
        None,
        description="Attendee response status",
        example=CalendarEventStatus.accepted,
    )


class Conference(BaseModel):
    id: int = Field(..., description="Conference ID", example=1)
    topic: Optional[str] = Field(None, description="Conference topic", example="Interview")
    auth_type: Optional[str] = Field(None, description="Conference venue", example="ZOOM")
    state: Optional[str] = Field(
        None,
    )
    start_time: Optional[datetime] = Field(
        None,
        description="Conference start",
        example=datetime(1970, 1, 1, 1, 1, 1),
    )
    end_time: Optional[datetime] = Field(
        None,
        description="Conference end",
        example=datetime(1970, 1, 1, 1, 1, 1),
    )
    timezone: Optional[str] = Field(None, description="Conference timezone", example="Africa/Accra")
    created: datetime = Field(
        ...,
        description="Conference creation datetime",
        example=datetime(1970, 1, 1, 1, 1, 1),
    )
    changed: Optional[datetime] = Field(
        None,
        description="Conference change datetime",
        example=datetime(1970, 1, 1, 1, 1, 1),
    )
    foreign: Optional[str] = Field(
        None,
        description="Foreign conference ID",
        example="conference_id",
    )
    link: Optional[str] = Field(
        None,
        description="Conference link",
        example="https://conference/link",
    )
    access_code: Optional[str] = Field(
        None,
        description="Conference access code",
        example="conference_code",
    )


class CalendarEventReminder(BaseModel):
    method: CalendarEventReminderMethod = Field(
        ...,
        description="Reminder method",
        example=CalendarEventReminderMethod.popup,
    )
    minutes: int = Field(
        ...,
        description="How many minutes in advance to remind about the event",
        example=1,
    )


class ApplicantLogCalendarEvent(BaseModel):
    id: int = Field(..., description="Calendar event ID", example=1)
    name: Optional[str] = Field(None, description="Event name", example="Test Name")
    description: Optional[str] = Field(
        None,
        description="Event description",
        example="Interview with John Doe",
    )
    status: CalendarEventStatus = Field(
        ...,
        description="Event status",
        example=CalendarEventStatus.accepted,
    )
    event_type: CalendarEventType = Field(
        ...,
        description="Event type",
        example=CalendarEventType.interview,
    )
    start: datetime = Field(
        ...,
        description="Event start date and time",
        example=datetime(1970, 1, 1, 1, 1, 1),
    )
    end: datetime = Field(
        ...,
        description="Event end date and time",
        example=datetime(1970, 1, 1, 1, 1, 1),
    )
    timezone: Optional[str] = Field(None, description="Event time zone", example="Africa/Accra")
    attendees: List[CalendarEventAttendee] = Field(
        [],
        description="Event attendees (participants)",
    )
    created: datetime = Field(
        ...,
        description="Date and time of event creation",
        example=datetime(1970, 1, 1, 1, 1, 1),
    )
    creator: Optional[CalendarEventCreator] = Field(None, description="Event creator")
    reminders: List[CalendarEventReminder] = Field(
        [],
        description="List of reminders",
    )
    all_day: bool = Field(
        ...,
        description="Flag indicating that the event is scheduled for the whole day",
        example=False,
    )
    foreign: Optional[str] = Field(None, description="Foreign event ID", example="f1")
    recurrence: Optional[List] = None
    etag: Optional[str] = Field(None, description="Event Etag", example=1633413621888)
    location: Optional[str] = Field(None, description="Event location", example="Some location")
    transparency: Transparency = Field(
        ...,
        description="Event transparency (availability)",
        example=Transparency.busy,
    )
    conference: Optional[Conference] = Field(None, description="Event conference data")
