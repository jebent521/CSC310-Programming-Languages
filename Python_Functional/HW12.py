'''
Write a decorator called printit that prints the name, input and output of the decorated function as a
sort of report which could be useful for debugging. Make sure to use functools wraps. The following
shows a silly example of printit in action:
The 'output 3' was due to the decorator. The second 3 is the return value of the function itself. The
decorated function doesn't just print its output, it actually returns it.
'''

from functools import wraps
def printit(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        arguments = ''
        for arg in args:
            arguments += (str(arg) + ', ')
        for k, v in kwargs.items():
            arguments += ('='.join((k, str(v))) + ', ')
        print(f.__name__, 'input:', arguments[:-2])
        print('output:', f(*args, **kwargs))
        return f(*args, **kwargs)
    return wrapper

@printit
def silly(a,b,**kwargs):
    return (a+b) % (1 + len(kwargs))

print(silly(5, 6, x=1, y=2, z=3))
