import math
class Quaternion:
    def __init__(self, a, b, c, d) -> None:
        if any(not isinstance(i, (int, float)) for i in [a,b,c,d]):
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
            else:                                       # note, no case for 0: don't add anything to the string
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
        return math.sqrt(self.a**2 + self.b**2 + self.c**2 + self.d**2)
    
    def norm(self):
        '''alias for abs(self)'''
        return abs(self)
    
    def conjugate(self):
        return Quaternion(self.a, -self.b, -self.c, -self.d)

    def inv(self):
        '''returns self ** -1'''
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
        if isinstance(other, (int, float)):
            other = Quaternion(other, 0, 0, 0)
        elif isinstance(other, complex):
            other = Quaternion(other.real, 0, other.imag, 0)
        elif isinstance(other, Quaternion):
            pass
        else:
            return NotImplemented
        return Quaternion(self.a - other.a, self.b - other.b, self.c - other.c, self.d - other.d)
    
    def __rsub__(self, other):  # ensure other is quaternion, then subtract
        if isinstance(other, (int, float)):
            other = Quaternion(other, 0, 0, 0)
        elif isinstance(other, complex):
            other = Quaternion(other.real, 0, other.imag, 0)
        else:
            return NotImplemented
        return Quaternion(other.a - self.a, other.b - self.b, other.c - self.c, other.d - self.d)
    
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
    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            other = Quaternion(other,0,0,0)
        elif isinstance(other, complex):
            other = Quaternion(other.real,0,other.imag,0)
        elif isinstance(other, Quaternion):
            pass
        else:
            return NotImplemented
        return self * other.inv()
    
    def __rtruediv__(self, other):
        if isinstance(other, (int, float)):
            other = Quaternion(other,0,0,0)
        elif isinstance(other, complex):
            other = Quaternion(other.real,0,other.imag,0)
        else:
            return NotImplemented
        return other / self