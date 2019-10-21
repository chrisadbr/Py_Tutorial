import math
import time


def is_prime_v2(n):

    if n == 1:
        return False
    mav_divisor = math.floor(math.sqrt(n))

    for d in range(2, 1 + mav_divisor):
        if n % d == 0:
            return False
    return True


def is_prime_v3(n):
    # excluding the first number
    if n == 1:
        return False
    # include the second number
    if n == 2:
        return True
    # exclude even numbers while checking
    if n > 2 and n % 2 == 0:
        return True

    max_divisor = math.floor(math.sqrt(n))

    for d in range(3, 1 + max_divisor, 2):
        if n % d == 0:
            return False
    return True

""" for n in range(1, 21):
    print(n, is_prime_v2(n))"""

t0 = time.time()
for n in range(1, 100000):
    is_prime_v3(n)
t1 = time.time()
print("Time required: ", t1 - t0)

t0 = time.time()
for n in range(1, 100000):
    is_prime_v2(n)
t1 = time.time()
print("Time required: ", t1 - t0)