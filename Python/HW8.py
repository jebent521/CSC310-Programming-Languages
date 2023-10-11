# Jonah Ebent, CSC310 Programming Languages, HW8, 10/13/2023
"""
1. Write a generator chunk() which takes a sliceable object such as a string or a list and an integer
    n and successively yields chunks of size n. For example, chunk('ABCDEFGHIJ',4) should yield
    'ABCD' and then 'EFGH' then 'IJ' Note that the last chunk yielded may be smaller than the
    previous chunks.
2. Write a generator which yields successive Fibonacci numbers: 1,1,2,3,5,8,13,21,34,... Note that
    this is an infinite generator. If you call it fib(), you can test it as follows: evaluate f = fib() and
    then print(next(f)) in a loop. Don't try list(f)!
"""
def chunk(s, n):
    for i in range(0,len(s),n):
        yield(s[i:i+n])

def fib():
    a, b = 1, 0
    while True:
        c = a + b
        a = b
        b = c
        yield c

print(list(chunk('ABCDEFGHIJ', 4)))
f = fib()
for i in range(10):
    print(next(f))