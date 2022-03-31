# Exercise 3, speed things up (hard)!

import timeit


# Bonus exercise - add an initialisation method to this class so that the state of some_param["counter"] is reset to
# 0, on every run of loop()
class Klass:
    some_param = {
        "counter": 0
    }

    def __init__(self):
        self.some_param["counter"] = 0

def loop():
    """
    This is slow, change it to run faster.
    :return:
    """

    klass = Klass()
    for _ in range(int(1)):
        klass.some_param["counter"] += 1

    # Leave this line in place.
    print(f"Some param value = {klass.some_param['counter']}")


# Change no code below!
if __name__ == "__main__":
    final = timeit.timeit(loop, number=10)
    print(f"Time taken = {final}")

# Bonus question: After the modifications explain what is going on in the back end, that has resulted in this speed up.
# Hint, decompile the bytecode for the original and your solution and examine it (look at the dis library), what is
# missing in the loop?
# Bonus question 2: What is the cost of doing this modification, IE what is used up in resources?