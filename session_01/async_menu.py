"""

"""
import asyncio
import time


async def chef(order_id):
    print("chef: {0} is preparing order".format(order_id))
    await asyncio.sleep(0.3) # <--- waiting
    print("chef: {0} order prepared".format(order_id))


async def waiter(n):
    print("Waiter: {0} is taking order".format(n))
    if n == 1:
        raise ValueError("Order can't be processed")
    await asyncio.sleep(0.1) # <--- waiting
    await chef(n)            # <--- waiting
    await asyncio.sleep(0.1) # <--- waiting
    print("Waiter: {0} is serving order".format(n))


if __name__ == "__main__":


    loop = asyncio.get_event_loop()

    ## ONE ORDER

    # start_time = time.time()
    #
    # loop.run_until_complete(waiter(1))
    #
    # loop.close()
    # end_time = time.time()
    #
    # print("\nTime taken to complete: {:4.4f}".format(end_time - start_time))


    ## FIVE ORDERS

    start_time = time.time()

    # tasks = asyncio.wait([asyncio.ensure_future(waiter(x)) for x in range(5)])

    tasks = asyncio.gather(*[asyncio.ensure_future(waiter(x)) for x in range(5)], return_exceptions=True)

    """
    Return a future aggregating results from the given coroutines or futures.
    All futures must share the same event loop.

    If `return_exceptions` is True, exceptions in the tasks are treated the same as successful results,
    and gathered in the result list;
    otherwise, the first raised exception will be immediately propagated to the returned future
    """

    loop.run_until_complete(tasks)
    loop.close()

    end_time = time.time()

    print("\nTime taken to complete: {:4.4f}".format(end_time - start_time))
