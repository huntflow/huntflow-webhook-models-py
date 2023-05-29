from enum import Enum


class WebhookEventType(str, Enum):
    APPLICANT = "APPLICANT"
    VACANCY = "VACANCY"
    VACANCY_REQUEST = "VACANCY-REQUEST"
    RESPONSE = "RESPONSE"
    OFFER = "OFFER"
    RECRUITMENT_EVALUATION = "RECRUITMENT-EVALUATION"
    SURVEY_QUESTIONARY = "SURVEY-QUESTIONARY"


class ApplicantWebhookActionType(str, Enum):
    ADD = "ADD"
    EDIT = "EDIT"
    DELETE = "DELETE"


class ApplicantLogType(str, Enum):
    ADD = "ADD"
    UPDATE = "UPDATE"
    VACANCY_ADD = "VACANCY-ADD"
    STATUS = "STATUS"
    COMMENT = "COMMENT"
    DOUBLE = "DOUBLE"
    AGREEMENT = "AGREEMENT"
    MAIL = "MAIL"
    RESPONSE = "RESPONSE"
    REMOVED = "REMOVED"
    VACANCY_REMOVE = "VACANCY-REMOVE"
    EXTERNAL_REMOVE = "EXTERNAL-REMOVE"
    EDIT = "EDIT"


class AgreementState(str, Enum):
    NOT_SENT = "not_sent"
    SENT = "sent"
    ACCEPTED = "accepted"
    DECLINED = "declined"


class SurveyType(str, Enum):
    TYPE_A = "type_a"
    TYPE_R = "type_r"


class VacancyState(str, Enum):
    OPEN = "OPEN"
    CLOSED = "CLOSED"
    HOLD = "HOLD"
    REOPEN = "REOPEN"
    VACANCY_REQUEST_ATTACH = "VACANCY_REQUEST_ATTACH"
    RESUME = "RESUME"
    CREATED = "CREATED"


class CalendarEventStatus(str, Enum):
    accepted = "accepted"
    declined = "declined"
    confirmed = "confirmed"
    tentative = "tentative"
    cancelled = "cancelled"
    needs_action = "needsAction"


class CalendarEventReminderMethod(str, Enum):
    popup = "popup"
    email = "email"


class CalendarEventType(str, Enum):
    interview = "interview"
    other = "other"


class Transparency(str, Enum):
    busy = "busy"
    free = "free"
