import pydantic


class Err2(pydantic.BaseModel):
    pass


class MyErrorContainer[ERR](pydantic.BaseModel):
    model_config = pydantic.ConfigDict(strict=True)
    err: ERR


if __name__ == "__main__":
    instance = MyErrorContainer[Err2](
        err=Err2  # Should error, argument is not an instance
    )
