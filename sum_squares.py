from time import time
from math import *

# d >= c >= b >= a
def list_nums(n):
    lst = []
    for a in range(floor(sqrt(n))+1):
        na = n - a**2
        for b in range(a, floor(sqrt(na))+1):
            nb = na - b**2
            for c in range(b, floor(sqrt(nb))+1):
                nc = nb - c**2
                d = floor(sqrt(nc))
                if d**2 == nc:
                    lst.append(a)
                    lst.append(b)
                    lst.append(c)
                    lst.append(d)
                    if len(lst) == 4:
                        return lst

# how to measure how long your function takes to run:
t1 = time()  # get start time
print(list_nums(512))  # run function
t2 = time()  # get end time
print(f"This took {t2 - t1} seconds")  # print result
