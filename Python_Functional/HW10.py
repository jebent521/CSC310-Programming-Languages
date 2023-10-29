"""
Jonah Ebent, 10/19/2023, CSC310 Programming Languages, HW10
clamp(a,b) (where a <= b) returns a function f(x), which returns a if x < a, x if a <= x <= b, or b if x > b
"""

def clamp(a, b):
    def f(x):
        if x < min(a,b):
            return min(a,b)
        if x > max(a,b):
            return max(a,b)
        else:
            return x
    return f
