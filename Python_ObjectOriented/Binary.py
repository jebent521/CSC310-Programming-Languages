#class of binary numbers

class Binary:
    def __init__(self,n):
        if isinstance(n,int):
            self._num = n
            if n >= 0:
                self.bin = bin(n)[2:]
            else:
                self.bin = '-' + bin(n)[3:]
        elif isinstance(n,str):
            self._num = int(n,2)
            self.bin = n
        else:
            raise ValueError(f"Can't convert {n} to a binary integer")

    def __repr__(self):
        return f"Binary('{self.bin}')"

    def __str__(self):
        return self.bin

    def __add__(self,other):
        if isinstance(other,Binary):
            return Binary(self._num + other._num)
        elif isinstance(other,int) or isinstance(other,str):
            other = Binary(other)
            return Binary(self._num + other._num)
        else:
            return NotImplemented

    def __radd__(self,other):
        if isinstance(other,int) or isinstance(other,str):
            other = Binary(other)
            return Binary(other._num + self._num)
        else:
            return NotImplemented

    def __eq__(self,other):
        return self._num == other._num

    def __ne__(self,other):
        return self._num != other._num

    def __lt__(self,other):
        return self._num < other._num

    def __le__(self,other):
        return self._num <= other._num

    def __gt__(self,other):
        return self._num > other._num

    def __ge__(self,other):
        return self._num >= other._num

    def __sub__(self,other):
        if isinstance(other,Binary):
            return Binary(self._num - other._num)
        elif isinstance(other,int) or isinstance(other,str):
            other = Binary(other)
            return Binary(self._num - other._num)
        else:
            return NotImplemented
    
    def __rsub__(self,other):
        if isinstance(other,int) or isinstance(other,str):
            other = Binary(other)
            return Binary(other._num - self._num)
        else:
            return NotImplemented
    
    def __mul__(self,other):
        if isinstance(other,Binary):
            return Binary(self._num * other._num)
        elif isinstance(other,int) or isinstance(other,str):
            other = Binary(other)
            return Binary(self._num * other._num)
        else:
            return NotImplemented

    def __rmul__(self,other):
        return self * other

    def __floordiv__(self,other):
        if isinstance(other,Binary):
            return Binary(self._num // other._num)
        elif isinstance(other,int) or isinstance(other,str):
            other = Binary(other)
            return Binary(self._num // other._num)
        else:
            return NotImplemented

    def __rfloordiv__(self,other):
        if isinstance(other,int) or isinstance(other,str):
            other = Binary(other)
            return Binary(other._num // self._num)
        else:
            return NotImplemented

    def __pow__(self,other):
        if isinstance(other, Binary):
            return Binary(self._num ** other._num)
        elif isinstance(other, int) or isinstance(other, str):
            other = Binary(other)
            return Binary(self._num ** other._num)
        else:
            return NotImplemented
        
    def __rpow__(self,other):
        if isinstance(other, int) or isinstance(other, str):
            other = Binary(other)
            return Binary(other._num ** self._num)
        else:
            return NotImplemented

    def __divmod__(self,other):
        if isinstance(other, Binary):
            pass
        elif isinstance(other, int) or isinstance(other, str):
            other = Binary(other)
        else:
            return NotImplemented
        quot, rem = divmod(self._num, other._num)
        return (Binary(quot), Binary(rem))
    
    def __rdivmod__(self, other):
        if isinstance(other, int) or isinstance(other, str):
            other = Binary(other)
        else:
            return NotImplemented
        quot, rem = divmod(other._num, self._num)
        return (Binary(quot), Binary(rem))