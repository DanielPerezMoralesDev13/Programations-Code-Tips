"""
Traceback (most recent call last):
  File "/home/d4nitrix13/Desktop/Python3-Tips/04 how to use never & NoReturn in python.py", line 1, in <module>
    from typing import NoReturn, Never
ImportError: cannot import name 'Never' from 'typing' (/usr/lib/python3.10/typing.py)
"""
# from typing import NoReturn, Never
from typing import NoReturn
from enum import Enum

# def func(msg) -> Never:
#     raise Exception(msg)


def func(msg) -> NoReturn:
    raise Exception(msg)

# arg: NoReturn
def asser_never(arg: Never) -> NoReturn:
    raise AssertionError("Expected code is unreacheable")

class State(Enum):
    OFF: int = 0
    ON: int = 1
    LIMBO: int = 2

def main() -> None:
    state: State = State.ON
    if state == State.ON:
        print("turned on!")
    elif state == State.OFF:
        print("turned off!")
    elif state == State.LIMBO:
        print("turned limbo!")
    else:
        assert_never(state)

if __name__ == "__main__":
    main()