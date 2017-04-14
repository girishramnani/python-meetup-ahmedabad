


def hello_sync(name):
    return "Hello {0}".format(name)


async def hello_async(name):
    return "Hello {0}".format(name)


def hello_old(name):
    yield "Hello {0}".format(name)


def run(coro):
    try:
        return coro.send(None)
    except StopIteration as e:
        return e.value


if __name__ == "__main__":
    print(hello_sync("lets nurture"))
    print(hello_async("lets nurture"))
    print(hello_old("lets nurture"))
    print(run(hello_async("lets nurture")))
    print(run(hello_old("lets nurture")))