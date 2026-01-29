from dataclasses import dataclass

import pydantic


class Err2(pydantic.BaseModel):
    pass


class MyErrorContainer[ERR](pydantic.BaseModel):
    err: ERR


instance = MyErrorContainer[Err2](
    err=Err2  # Incorrectly does not error on pyrefly 0.50.1
)


@dataclass
class Err2Dc:
    pass


@dataclass
class MyErrorContainerDc[ERR]:
    err: ERR


instance = MyErrorContainer[Err2Dc](
    err=Err2Dc  # Incorrectly does not error on pyrefly 0.50.1
)
