"""

"""
import time


def chef(order_id):
    print("chef: {0} is preparing order".format(order_id))
    time.sleep(0.3) # <--- waiting
    print("chef: {0} order prepared".format(order_id))


def waiter(n):
    print("Waiter: {0} is taking order".format(n))
    time.sleep(0.1) # <--- waiting
    chef(n)         # <--- waiting
    time.sleep(0.1) # <--- waiting
    print("Waiter: {0} is serving order".format(n))


if __name__ == "__main__":

    ## ONE ORDER
    start_time = time.time()

    waiter(1)

    end_time = time.time()

    print("\nTime taken to complete: {:4.4f}".format(end_time - start_time))

    ## FIVE ORDERs

    # start_time = time.time()
    #
    # for x in range(5):
    #     waiter(x)
    #
    # end_time = time.time()
    #
    # print("\nTime taken to complete: {:4.4f}".format(end_time - start_time))