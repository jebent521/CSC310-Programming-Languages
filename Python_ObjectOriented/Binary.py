class Binary:
    def __init__(self,n) -> None:
        if isinstance(n,int):
            self._num = n
            if n >= 0:
                self.bin = bin(n)[2:]
            else:
                self.bin = '-' + bin(n)[3:]
        elif isinstance(n, str):
            self._num = int(n, 2)
            self.bin = n
        else:
            raise ValueError(f"Can't convert {n} to a binary integer")
        
    def __repr__(self) -> str:
        return f"Binary('{self.bin}')"
    
    def __str__(self) -> str:
        return self.bin
    
    # add two objects of your class, or modify to work more flexibly
    # self + other
    def __add__(self, other):   # 'other' is a convention
        if isinstance(other, Binary):
            return Binary(self._num + other._num)
        elif isinstance(other, int) or isinstance(other, str):
            other = Binary(other)
            return Binary(self._num + other._num)
        else:
            return NotImplemented
            # custom error message for particular call
            # e.g. Binary('110100101') + 3.14
            # TypeError: unsupported operand type(s) for +: 'Binary' and 'float'

    # right addition, where object of class is on right side of operator
    # other + self 
    def __radd__(self, other):
        if isinstance(other, int) or isinstance(other, str):
            other = Binary(other)
            return Binary(other._num + self._num)
        else:
            return NotImplemented
        # it would be redundant to implement if other is a Binary, because that would have __add__

    # override the += operator, used when += is to be implemented by mutating self
    # unneccessary for immutable objects, bc Python will interpret a += b as a = a + b
    # self += other
    def __iadd__(self, other):
        # the following keeps the ID of self
        """
        if isinstance(other, Binary):
            pass
        elif isinstance(other, int) or isinstance(other, str):
            other = Binary(other)
        else:
            return NotImplemented
        self._num = self._num + other._num
        # MISSING CODE, SEE SLIDES
        return self
        """
        # the following changes the ID of self
        return self + other
    # we could just delete __iadd__ since once __add__ is defined, a += b still works

    def __eq__(self, other):
        return self._num == other._num
    #...
    