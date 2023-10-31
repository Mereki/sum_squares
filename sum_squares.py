from time import time
from math import *

# d >= c >= b >= a
def list_nums(n):
    for a in range(floor(sqrt(n))+1):
        na = n - a**2
        for b in range(a, floor(sqrt(na))+1):
            nb = na - b**2
            for c in range(b, floor(sqrt(nb))+1):
                nc = nb - c**2
                d = floor(sqrt(nc))
                if d**2 == nc:
                    return [a, b, c, d]  
    
# how to measure how long your function takes to run:
t1 = time()  # get start time
print(list_nums(512))  # run function
t2 = time()  # get end time
print(f"This took {t2 - t1} seconds")  # print result
