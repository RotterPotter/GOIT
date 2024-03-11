import math
import time



def factorize(*number):
    list_of_lists = list()

    for n in number:
        factors = [1]

        for t in range(2, (math.ceil((n / 2) + 1))):
            if n % t == 0:
                factors.append(t)

        factors.append(n)

        list_of_lists.append(factors)

    return list_of_lists

start = time.time()
a, b, c, d  = factorize(128, 255, 99999, 10651060)
end = time.time()
print(end-start)

assert a == [1, 2, 4, 8, 16, 32, 64, 128]
assert b == [1, 3, 5, 15, 17, 51, 85, 255]
assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106, 1521580, 2130212, 2662765, 5325530, 10651060]
