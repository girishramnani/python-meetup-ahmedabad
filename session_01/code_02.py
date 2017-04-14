"""


"""

def squares():
    for x in range(1, 5):
        yield x**x

def weekdays():
    yield "Sunday"
    yield "Monday"
    yield "Tuesday"
    yield "Wednesday"
    yield "Thrusday"
    yield "Friday"
    yield "Saturday"

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