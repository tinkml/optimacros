import dataclasses
from typing import Union


@dataclasses.dataclass
class FactorialData:
    number: int

    @classmethod
    def from_raw_msg(cls, msg: Union[str, int]) -> "FactorialData":
        if isinstance(msg, str) and not msg.isdigit():
            raise TypeError("Value is not a number")

        return cls(number=int(msg))
