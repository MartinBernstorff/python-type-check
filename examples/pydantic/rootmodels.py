import pydantic


class RootOne(pydantic.RootModel[str]):
    pass


class RootTwo(pydantic.RootModel[str]):
    pass


class Base(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(strict=True)

    value: RootOne


if __name__ == "__main__":
    r1 = Base(value=RootOne("hello"))

    r2 = Base(value=RootTwo("hello"))  # This should raise a validation error
