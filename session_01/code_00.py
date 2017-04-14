
def my_printer():
    while True:
        x = yield
        print("Got {0}".format(x))

def square():
    while True:
        x = yield
        print("Got {0}".format(x))
        yield x ** 2


def countdown(n):
    while n > 0:
        yield n # <-- Instead of returning a value, you generate a series of values (using the yield statement)
        n -= 1



if __name__ == "__main__":
    p = my_printer()
    next(p)                 # <-- reach to the first yield

    x = p.send("homework")
    print(x)

    x = p.send("news")
    print(x)

    x = p.send("bills")
    print(x)

    print("**" * 10)

    val = square()

    next(val)               # <-- reach to the first yield
    x  = val.send(3)        # 3 goes to the x variable
    print(x)

    next(val)
    x = val.send(4)
    print(x)

    next(val)
    x = val.send(5)
    print(x)

    print("**" * 10)

    for i in countdown(5):
        print(i)