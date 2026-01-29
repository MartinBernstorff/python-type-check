import pydantic
import pytest
from pydantic import Field


class UserName(pydantic.RootModel[str]):
    root: str = Field(..., min_length=3, max_length=150)


class CreateUserRequest(pydantic.BaseModel):
    """Request schema for creating a user."""

    username: UserName


def test_rootmodel_usage():
    result = CreateUserRequest(username=UserName("MyName"))
    assert result.username.root == "MyName"


def test_invalid_name():
    with pytest.raises(pydantic.ValidationError):
        CreateUserRequest(username=UserName("."))
