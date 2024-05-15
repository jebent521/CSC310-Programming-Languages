#===========================================================#
# 1: Create a Mediant Class
#===========================================================#
class Mediant:
    def __init__(self, a, b):
        if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
            raise ValueError("Arguments must be numbers")
        self.a = a
        self.b = b

    def __repr__(self):
        return f"Mediant({self.a}, {self.b})"
    
    def __str__(self):
        return f"{self.a}/{self.b}"
    
    def __add__(self, other):
        if not isinstance(other, Mediant):
            return NotImplemented
        return Mediant(self.a + other.a, self.b + other.b)
    
    def __sub__(self, other):
        if not isinstance(other, Mediant):
            return NotImplemented
        return Mediant(self.a - other.a, self.b - other.b)
    
    def __mul__(self, other):
        if not isinstance(other, Mediant):
            return NotImplemented
        return Mediant(self.a * other.a, self.b * other.b)
    
    def __truediv__(self, other):
        if not isinstance(other, Mediant):
            return NotImplemented
        return Mediant(self.a / other.a, self.b / other.b)
    
    def __eq__(self, __value):
        if not isinstance(__value, Mediant):
            return False
        return (self.a == __value.a and self.b == __value.b)
    
#===========================================================#
# 2: Various Uses of *
#===========================================================#
x = 2 * 4               # x is assigned the 8, product of 2 and 4

myList = [1,2,3,4]
def Max(a,b,c,d):       # the Max function requires 4 positional arguments
    return max(a,b,c,d)
Max(*myList)            # Max(myList) won't work because that's only one argument, but Max(*myList) does because it unpacks myList

#===========================================================#
# 3. Create a ReducedMediant Class that inherits from Mediant
#===========================================================#
from math import gcd
class ReducedMediant(Mediant):
    def __init__(self, a, b):
        if not isinstance(a, int) or not isinstance(b, int):
            raise ValueError("a and b must be integers")
        super().__init__(a, b)
        self.__reduce()

    def __reduce(self):
        GCD = gcd(self.a, self.b)
        self.a = self.a // GCD
        self.b = self.b // GCD
    
    def __repr__(self):
        return f"ReducedMediant({self.a}, {self.b})"
    
    def __add__(self, other):
        if not isinstance(other, Mediant):
            return NotImplemented
        return ReducedMediant(self.a + other.a, self.b + other.b)

    def __sub__(self, other):
        if not isinstance(other, Mediant):
            return NotImplemented
        return ReducedMediant(self.a - other.a, self.b - other.b)
    
    def __mul__(self, other):
        if not isinstance(other, Mediant):
            return NotImplemented
        return ReducedMediant(self.a * other.a, self.b * other.b)
    
    def __truediv__(self, other):
        if not isinstance(other, Mediant):
            return NotImplemented
        return ReducedMediant(self.a // other.a, self.b // other.b)

#===========================================================#
# 4. Regex for Phone Numbers of the form (###)###-####
#===========================================================#
import re
pat = r'\(\d{3}\)\d{3}-\d{4}'
myMatch = re.search(pat, "(740)284-5277")   # will match
myMatch = re.search(pat, "7402845277")      # won't match

#===========================================================#
# 7. Create a Deck Class that inherits from abc.Collection
#===========================================================#
from collections.abc import Collection
from random import shuffle
from itertools import product
class Deck(Collection):
    def __init__(self) -> None:
        values = ['A', *list(range(2, 11)), 'J', 'Q', 'K']
        suits = ['S', 'C', 'H', 'D']
        self.deck = list(product(values, suits))
        shuffle(self.deck)
        
    def __contains__(self, __x):
        return __x in self.deck

    def __iter__(self):
        for card in self.deck:
            yield card
    
    def __len__(self):
        return len(self.deck)

#===========================================================#
# 7. Named Tuple definition of Quaternions
#===========================================================#
from collections import namedtuple
Quaternion = namedtuple('Quaternion', ['real', 'i', 'j', 'k'])
q = Quaternion(2,3,-1,4)