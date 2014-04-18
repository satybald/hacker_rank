#!/usr/bin/python
import math
"""
You are given an integer N, can you check if the number is an element of fibonacci series? The first few elements of fibonacci series are 0,1,1,2,3,5,8,13. A fibonacci series is one where every element is a sum of the previous two elements in the series. The first two elements are 0 and 1.

Notes:
[1] http://en.wikipedia.org/wiki/Isqrt
"""
list_in = [11, 5, 8, 77]
dict_f = dict()

def is_perfect_num(N):
    x = math.sqrt(N)
    print x, N
    return int(x +0.5) **2 == N

def check_fib(N):
    return is_perfect_num(5*N*N + 4) or is_perfect_num(5*N*N - 4)

def is_fib(n):
    if check_fib(n):
        return "IsFibo"
    else:
        return "IsNotFibo"

for y in list_in:
    print is_fib(y)