''' Jonah Ebent, Dr. Coleman, CSC310 Programming Languages, 12/12/23
Quaternion.py contains a class that defines quaternions, the number system extending the complex numbers.
It overloads addition, subtraction, multiplication, division, and absolute value.
I chose not to implement __iadd__, __isub__, etc. because it is not necessary for the quaternion to have
    the same location in memory before and after these operations.
Some of the quaternion-specific functions are:
    norm(),         which returns the size of the quaternion (alias of abs()),
    conjugate(),    which returns the quaternion's conjugate (a - bi - cj - dk), and
    inv(),          which returns the multiplicative inverse of the quaternion (equivalent to q ** -1)
I used Wikipedia for the formulas (https://en.wikipedia.org/wiki/Quaternion)
'''

import math
class Quaternion:
    def __init__(self, a, b, c, d) -> None:
        '''a, b, c, and d must be ints or floats'''
        if any(not isinstance(i, (int, float)) for i in [a,b,c,d]): # ensure a,b,c,d are numbers
            raise ValueError('Coefficients must be numbers.')
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def __repr__(self) -> str:
        return f'Quaternion({self.a}, {self.b}, {self.c}, {self.d})'
    
    def __str__(self) -> str:
        def signOf(num):            # helper function that returns the sign of the number it's given
            if num == 0:
                return 0
            return num / abs(num)
        string = ''
        for num, dim in zip([self.a, self.b, self.c, self.d], ['', 'i', 'j', 'k']):
            if len(string) == 0 and num != 0:           # ensures you don't get any plus signs at the beginning of the expression
                    string += f'{str(num)}{dim}'
            else:                                       # note, no case for num = 0: don't add anything to the string
                match signOf(num):
                    case -1.0:
                        string += f'{str(num)}{dim}'    # num provides the negative sign for subtraction
                    case 1.0:                           # add a plus sign for addition when num is positive
                        string += f'+{str(num)}{dim}'                                                        
        if len(string) == 0:                            # if nothing is in the string, return 0
            return '0'
        return string
    
    # QUATERNION OPERATIONS
    def __abs__(self):
        '''Returns the size of the quaternion'''
        return math.sqrt(self.a**2 + self.b**2 + self.c**2 + self.d**2)
    
    def conjugate(self):
        '''Returns (a-bi-cj-dk)'''
        return Quaternion(self.a, -self.b, -self.c, -self.d)

    def inv(self):
        '''Returns self ** -1'''
        den = pow(abs(self), 2)
        a = self.a / den
        b = -self.b / den
        c = -self.c / den
        d = -self.d / den
        return Quaternion(a,b,c,d)

    # ADDITION
    def __add__(self, other):
        if isinstance(other, (int, float)):
            other = Quaternion(other, 0, 0, 0)
        elif isinstance(other, complex):
            other = Quaternion(other.real, 0, other.imag, 0)
        elif isinstance(other, Quaternion):
            pass
        else:
            return NotImplemented
        return Quaternion(self.a + other.a, self.b + other.b, self.c + other.c, self.d + other.d)        
    
    def __radd__(self, other):
        return self + other     # works because addition is commutative

    # SUBTRACTION
    def __sub__(self, other):   # ensure other is quaternion, then subtract
        return self + -1 * other
    
    def __rsub__(self, other):  # ensure other is quaternion, then subtract
        return other + -1 * self
    
    # MULTIPLICATION
    def __mul__(self, other):   # ensure other is quaternion, then use hamilton product
        if isinstance(other, (int, float)):
            other = Quaternion(other, 0, 0, 0)
        elif isinstance(other, complex):
            other = Quaternion(other.real, 0, other.imag, 0)
        elif isinstance(other, Quaternion):
            pass
        else:
            return NotImplemented
        a = self.a*other.a - self.b*other.b - self.c*other.c - self.d*other.d
        b = self.a*other.b + self.b*other.a + self.c*other.d - self.d*other.c
        c = self.a*other.c - self.b*other.d + self.c*other.a + self.d*other.b
        d = self.a*other.d + self.b*other.c - self.c*other.b + self.d*other.a
        return Quaternion(a,b,c,d)
    
    def __rmul__(self, other): # hamilton product is not commutative. ensure other is quaternion, then multiply as normal
        if isinstance(other, (int, float)):
            other = Quaternion(other, 0, 0, 0)
        elif isinstance(other, complex):
            other = Quaternion(other.real, 0, other.imag, 0)
        else:
            return NotImplemented
        return other * self

    # DIVISION
    def __truediv__(self, other):   # ensure other is quaternion, then multiply by inverse of other
        if isinstance(other, (int, float)):
            other = Quaternion(other,0,0,0)
        elif isinstance(other, complex):
            other = Quaternion(other.real,0,other.imag,0)
        elif isinstance(other, Quaternion):
            pass
        else:
            return NotImplemented
        return self * other.inv()
    
    def __rtruediv__(self, other):  # ensure other is quaternion, then divide as normal
        return other * self.inv()