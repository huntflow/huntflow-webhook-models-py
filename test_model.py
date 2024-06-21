from pydantic import BaseModel, ConfigDict

from huntflow_webhook_models import RecruitmentEvaluationHookRequest

# BaseModel.model_config = ConfigDict(extra="forbid")


class B(BaseModel):
    b: int


class A(BaseModel):
    a: int
    b: B


# a = A.model_validate({"a": 1, "b": {"b": 1, "l": 5675}})
# print(a)
# print(a.model_config)
# print(a.b.model_config)

a = RecruitmentEvaluationHookRequest
print(a.model_config)
