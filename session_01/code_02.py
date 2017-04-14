"""


"""

from code_01 import *

def run(coro):
    try:
        return coro.send(None)
    except StopIteration as e:
        return e.value


if __name__ == "__main__":
    result = squares()

    print(run(result))
    print(run(result))
    print(run(result))
    print(run(result))
    print(run(result))