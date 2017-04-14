
"""
ITERATORS vs GENERATORS

*   Generatros are iterators; but only ONE iteration is allowed

next(iterator[, default])

    Return the next item from the iterator.
    If default is given and the iterator is exhausted, it is returned instead of raising StopIteration.

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

if __name__ == "__main__":


    result = squares()

    print(result.send(None))
    print(result.send(None))
    print(result.send(None))
    print(result.send(None))
    print(result.send(None))

    # print(result)
    # print(next(result))
    # print(next(result))
    # print(next(result))
    # print(next(result))
    # print(next(result))
    # print(next(result))

    days = weekdays()

    # print(days.__next__())
    # print(days.__next__())
    # print(days.__next__())
    # print(days.__next__())
    # print(days.__next__())
    # print(days.__next__())
    # print(days.__next__())
    # print(days.__next__())

    # print(next(days))
    # print(next(days))
    # print(next(days))
    # print(next(days))
    # print(next(days))
    # print(next(days))
    # print(next(days))
    # print(next(days))