"""Using a function closure and the cache decorator, write a function called rand_map where rand_map(n)
returns a random map on 0,1,2,...,n-1. If f = rand_map(100) (for example) then f(5) should be a random
number in the range 0 to 99. The first time f(5) is called it is chosen randomly. Subsequent calls to f(5)
should return the same value. Hint: very little code is required"""

from functools import cache
from random import randint
def rand_map(n):
    @cache
    def f(x):
        return randint(0, n-1)
    return f

