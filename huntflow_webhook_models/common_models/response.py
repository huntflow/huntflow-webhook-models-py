from datetime import datetime
from typing import Any, List, Optional, Union

from pydantic.fields import Field
from pydantic.main import BaseModel

from huntflow_webhook_models.common_models.hf_base import AccountSource
from huntflow_webhook_models.common_models.vacancy import Vacancy
from huntflow_webhook_models.consts import (
    ApplicantResponseExternalStatus,
    PrecisionTypes,
    VacancyExternalPublishStatus,
)


class PhotoData(BaseModel):
    small: Optional[str] = Field(
        None,
        description="Small image url",
        examples=["https://example.com/image_small.png"],
    )
    medium: Optional[str] = Field(
        None,
        description="Medium image url",
        examples=["https://example.com/image_medium.png"],
    )
    large: Optional[str] = Field(
        None,
        description="Large image url",
        examples=["https://example.com/image_large.png"],
    )
    external_id: Optional[str] = Field(None, description="Photo external ID", examples=["12"])
    description: Optional[str] = Field(
        None,
        description="Photo description",
        examples=["Applicant's photo"],
    )
    source: Optional[str] = Field(
        None,
        description="Photo's source url",
        examples=["https://example.com/photo_source.png"],
    )
    id: Optional[int] = Field(None, description="Huntflow photo ID", examples=[10])


class DateWithPrecision(BaseModel):
    year: Optional[int] = Field(None, description="Year", examples=[2021])
    month: Optional[int] = Field(None, description="Month", examples=[12])
    day: Optional[int] = Field(None, description="Day", examples=[12])
    precision: PrecisionTypes = Field(
        ...,
        description="Precision type",
        examples=[PrecisionTypes.day],
    )


class TextBlock(BaseModel):
    header: Optional[str] = Field(None, description="Text block header", examples=["About header"])
    body: Optional[str] = Field(None, description="Text block body", examples=["About body"])


class PersonalInfo(BaseModel):
    photo: Optional[PhotoData] = Field(None, description="Urls for resume photo")
    first_name: Optional[str] = Field(None, description="First name", examples=["John"])
    middle_name: Optional[str] = Field(None, description="Middle name", examples=["Abraham"])
    last_name: Optional[str] = Field(None, description="Last name", examples=["Doe"])
    birth_date: Optional[DateWithPrecision] = Field(None, description="Date of birth")
    text_block: Optional[TextBlock] = Field(None, description='Additional "About" info')


class ExternalEntity(BaseModel):
    id: Optional[Union[int, str]] = Field(
        None,
        description="Entity ID in Huntflow system",
        examples=[1],
    )
    external_id: Optional[str] = Field(None, description="Entity external ID", examples=["1"])
    name: Optional[str] = Field(None, description="Entity name", examples=["name"])


class Specialization(ExternalEntity):
    profarea_id: Optional[str] = Field(
        None,
        description="Specialization ID in Huntflow system",
        examples=["10"],
    )
    external_profarea_id: Optional[str] = Field(
        None,
        description="Specialization external ID",
        examples=["external_10"],
    )
    prefarea_name: Optional[str] = Field(
        None,
        description="Specialization name",
        examples=["Sales"],
    )


class Area(BaseModel):
    country: Optional[ExternalEntity] = Field(None, description="Country")
    city: Optional[ExternalEntity] = Field(None, description="City")
    metro: Optional[ExternalEntity] = Field(None, description="Metro station")
    address: Optional[str] = Field(None, description="Full address", examples=["Washington DC"])
    lat: Optional[float] = Field(None, description="Latitude", examples=[38.8951])
    lng: Optional[float] = Field(None, description="Longitude", examples=[-77.0364])


class Skill(BaseModel):
    title: str = Field(..., description="Skill name", examples=["English language"])


class Experience(BaseModel):
    position: Optional[str] = Field(None, description="Position", examples=["Manager"])
    date_from: Optional[DateWithPrecision] = Field(None, description="Experience start date")
    date_to: Optional[DateWithPrecision] = Field(None, description="Experience end date")
    company: Optional[str] = Field(None, description="Company name", examples=["Company"])
    url: Optional[str] = Field(None, description="Company's url", examples=["https://example.com"])
    area: Optional[Area] = Field(None, description="Experience area")
    industries: Optional[List[ExternalEntity]] = Field(
        None,
        description="List of experience industries",
    )
    description: Optional[str] = Field(
        None,
        description="Experience description",
        examples=["I worked as a manager"],
    )
    skills: Optional[List[Skill]] = Field(None, description="List of skills")


class BaseEducationInfo(BaseModel):
    name: Optional[str] = Field(None, description="Education name", examples=["Higher"])
    description: Optional[str] = Field(
        None,
        description="Education description",
        examples=["I have a higher education"],
    )
    date_from: Optional[DateWithPrecision] = Field(None, description="Education start date")
    date_to: Optional[DateWithPrecision] = Field(None, description="Education end date")
    area: Optional[Area] = Field(None, description="Education area")


class EducationInfoWithResult(BaseEducationInfo):
    result: Optional[str] = Field(None, description="Education result", examples=["Completed"])


class ExtendedEducationInfo(BaseEducationInfo):
    faculty: Optional[str] = Field(None, description="Faculty name", examples=["Mathematics"])
    form: Optional[ExternalEntity] = Field(None, description="Education form data")


class Attestation(BaseModel):
    date: Optional[DateWithPrecision] = Field(None, description="Attestation date")
    name: Optional[str] = Field(None, description="Attestation name", examples=["name"])
    organization: Optional[str] = Field(
        None,
        description="Attestation organization",
        examples=["organization"],
    )
    description: Optional[str] = Field(
        None,
        description="Attestation description",
        examples=["description"],
    )
    result: Optional[str] = Field(None, description="Attestation result", examples=["resukt"])


class Education(BaseModel):
    level: Optional[ExternalEntity] = Field(None, description="Education level")
    higher: Optional[List[ExtendedEducationInfo]] = Field(
        None,
        description="List of higher education institutions",
    )
    vocational: Optional[List[ExtendedEducationInfo]] = Field(
        None,
        description="List of vocational education institutions",
    )
    elementary: Optional[List[BaseEducationInfo]] = Field(
        None,
        description="List of elementary education institutions",
    )
    additional: Optional[List[EducationInfoWithResult]] = Field(
        None,
        description="List of additional education institutions",
    )
    attestation: Optional[List[Attestation]] = Field(None, description="List of attestations")


class Certificate(BaseModel):
    name: Optional[str] = Field(None, description="Name of certificate", examples=["Certificate"])
    organization: Optional[str] = Field(
        None,
        description="The organization that issued the certificate",
        examples=["Certificate organnization"],
    )
    description: Optional[str] = Field(
        None,
        description="Certificate description",
        examples=["Certificate for John Doe"],
    )
    url: Optional[str] = Field(
        None,
        description="Certificate url",
        examples=["https://example.com/certificate_john_doe.pdf"],
    )
    area: Optional[Area] = Field(None, description="Area of issue of the certificate")
    date: Optional[DateWithPrecision] = Field(None, description="Date of issue of the certificate")


class ContactPhone(BaseModel):
    country: str = Field(..., description="Contact phone country", examples=["Japan"])
    city: str = Field(..., description="Contact phone city", examples=["Tokyo"])
    number: str = Field(..., description="Contact phone number", examples=["+ 1 999 888-77-66"])
    formatted: str = Field(..., description="Contact phone format", examples=["+1 (XXX) XXX-XX-XX"])


class Contact(BaseModel):
    type: Optional[ExternalEntity] = Field(None, description="Contact type")
    value: Optional[str] = Field(None, description="Contact value", examples=["89999999999"])
    preferred: Optional[bool] = Field(
        None,
        description="This is the preferred method of communication",
        examples=["true"],
    )
    full_value: Optional[ContactPhone] = Field(
        None,
        description="If contact is a phone number - additional data about it",
    )


class Relocation(BaseModel):
    type: Optional[ExternalEntity] = Field(None, description="Type of relocation")
    area: Optional[List[Area]] = Field(None, description="List of areas for relocation")


class Language(ExternalEntity):
    level: Optional[ExternalEntity] = Field(None, description="Language proficiency level")


class Military(BaseModel):
    date_from: Optional[DateWithPrecision] = Field(None, description="Military service start date")
    date_to: Optional[DateWithPrecision] = Field(None, description="Military service end date")
    area: Optional[Area] = Field(None, description="Military service area")
    unit: Optional[dict] = Field(
        None,
        description="Military service unit",
        examples=[{"name": "Infantry", "external_id": 3336026}],
    )


class SocialRating(BaseModel):
    kind: Optional[str] = Field(None, description="Social rating kind", examples=["Some kind"])
    stats: Optional[Any] = Field(None, description="Social rating stats", examples=["1"])
    tags: Optional[List[str]] = Field(None, description="Social rating stats", examples=[["tag1"]])
    url: Optional[str] = Field(None, description="Social rating url", examples=["https://url"])
    login: Optional[str] = Field(None, description="Social rating login", examples=["login"])
    registered_at: Optional[str] = Field(None, description="ISO datetime")


class Salary(BaseModel):
    amount: Optional[float] = Field(None, description="Salary amount", examples=[100.0])
    currency: Optional[str] = Field(None, description="Salary currency", examples=["USD"])


class Recommendation(BaseModel):
    value: Optional[str] = Field(None, description="Recommendation", examples=["Nice"])
    date: Optional[DateWithPrecision] = Field(None, description="Date of recommendation")
    name: Optional[str] = Field(None, description="Name to whom recommendation", examples=["John"])
    position: Optional[str] = Field(None, description="Position", examples=["Manager"])
    organization: Optional[str] = Field(
        None,
        description="Organization name",
        examples=["Test organization"],
    )
    contact: Optional[str] = Field(None, description="Contact", examples=["89999999999"])


class SimplePhoto(BaseModel):
    url: Optional[str] = Field(None, description="Photo url", examples=["https://url"])
    original: Optional[str] = Field(None, description="Photo original", examples=["photo"])


class Additional(BaseModel):
    name: Optional[str] = Field(None, description="Name of additional info", examples=["name"])
    description: Optional[str] = Field(
        None,
        description="Description of additional info",
        examples=["description"],
    )


class Resume(BaseModel):
    personal_info: Optional[PersonalInfo] = Field(None, description="Personal info")
    source_url: Optional[str] = Field(
        None,
        description="Resume url to external job site",
        examples=["https://example.com/resume"],
    )
    position: Optional[str] = Field(None, description="Resume header", examples=["Manager"])
    specialization: Optional[List[Specialization]] = Field(None, description="Specializations")
    skill_set: Optional[List[str]] = Field(
        None,
        description="List of skills",
        examples=[["English language"]],
    )
    gender: Optional[ExternalEntity] = Field(None, description="Gender")
    experience: Optional[List[Experience]] = Field(None, description="Work experiences")
    education: Optional[Education] = Field(None, description="Education")
    certificate: Optional[List[Certificate]] = Field(None, description="Certificates")
    portfolio: Optional[List[PhotoData]] = Field(None, description="Portfolio")
    contact: Optional[List[Contact]] = Field(None, description="List of contacts")
    area: Optional[Area] = Field(None, description="Living area")
    relocation: Optional[Relocation] = Field(None, description="Relocation info")
    citizenship: Optional[List[ExternalEntity]] = Field(None, description="Citizenship")
    work_permit: Optional[List[ExternalEntity]] = Field(
        None,
        description="List of countries with work permission",
    )
    language: Optional[List[Language]] = Field(None, description="Language proficiency")
    wanted_salary: Optional[Salary] = Field(None, description="Desired salary")
    work_schedule: Optional[List[ExternalEntity]] = Field(None, description="Work schedules")
    business_trip_readiness: Optional[ExternalEntity] = Field(
        None,
        description="Readiness for business trips",
    )
    recommendations: Optional[List[Recommendation]] = Field(
        None,
        description="List of recommendations",
    )
    has_vehicle: Optional[bool] = Field(
        None,
        description="Ownership of vehicle",
        examples=[False],
    )
    driver_license_types: Optional[List[str]] = Field(
        None,
        description="List of available driver's licenses",
        examples=[["A1", "B1"]],
    )
    military: Optional[List[Military]] = Field(None, description="Military service")
    social_ratings: Optional[List[SocialRating]] = Field(None, description="Social ratings")
    photos: Optional[List[SimplePhoto]] = Field(None, description="Photos")
    additionals: Optional[List[Additional]] = Field(
        None,
        description="Some additional info related to resume",
    )
    wanted_place_of_work: Optional[str] = Field(
        None,
        description="Desired place of work",
        examples=["New York"],
    )
    updated_on_source: Optional[DateWithPrecision] = Field(
        None,
        description="Date of resume update in the source",
    )
    travel_time: Optional[ExternalEntity] = Field(None, description="Preferred travel time")


class ApplicantExternalResponse(BaseModel):
    id: int = Field(..., description="Applicant source ID", examples=[1])
    created: datetime = Field(
        ...,
        description="The datetime when the response was stored in the database",
        examples=[datetime(1970, 1, 1, 1, 1, 1)],
    )
    foreign: str = Field(
        ...,
        description="Foreign applicant external ID",
        examples=["external-9-23"],
    )
    resume: Optional[Resume] = Field(None, description="Applicant resume")
    state: Optional[ApplicantResponseExternalStatus] = Field(
        None,
        description="Response state",
        examples=[ApplicantResponseExternalStatus.TAKEN],
    )
    updated: datetime = Field(
        ...,
        description="Datetime of response creation/update on the career site",
        examples=[datetime(1980, 1, 1, 1, 1, 1)],
    )


class AccountVacancyExternal(BaseModel):
    id: int = Field(..., description="Account vacancy external ID", examples=[1])
    account_source: AccountSource = Field(..., description="Vacancy account source")
    auth_type: str = Field(..., description="Authentication type", examples=["NATIVE"])
    name: str = Field(..., description="Account vacancy external name", examples=["HeadHunter"])


class VacancyExternal(BaseModel):
    id: int = Field(..., description="Vacancy external ID", examples=[1])
    account_vacancy_external: AccountVacancyExternal = Field(
        ...,
        description="Account vacancy external",
    )
    data: str = Field(
        ...,
        description="Additional data",
        examples=["comment"],
    )
    foreign: str = Field(..., description="Foreign vacancy external ID", examples=["12345"])
    state: Optional[VacancyExternalPublishStatus] = Field(
        None,
        description="Vacancy external publish status",
        examples=[VacancyExternalPublishStatus.PUBLISHED],
    )
    vacancy: Vacancy = Field(..., description="Vacancy data")
