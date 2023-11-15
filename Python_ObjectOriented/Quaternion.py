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
        def signOf(num):
            if num == 0:
                return 0
            return num / abs(num)
        string = ''
        if self.a != 0:
            string += str(self.a)
        match signOf(self.b):
            case -1:
                string += f'{str(self.b)}i'
            case 0:
                pass
            case 1:
                string += f'+{str(self.b)}i'
        match signOf(self.c):
            case -1:
                string += f'{str(self.c)}j'
            case 0:
                pass
            case 1:
                string += f'+{str(self.c)}j'
        match signOf(self.d):
            case -1:
                string += f'{str(self.d)}k'
            case 0:
                pass
            case 1:
                string += f'+{str(self.d)}k'
        return string
    def __abs__(self):
        pass
    
    def __add__(self):
        pass
    
    def __iadd__(self):
        pass
    
    def __sub__(self):
        pass
    
    def __isub__(self):
        pass
    
    def __mul__(self):
        pass
    
    def __imul__(self):
        pass
    
    def __rmul__(self):
        pass
    
    def __truediv__(self):
        pass
    
    def __itruediv__(self):
        pass
    
    def conjugate(self):
        pass
    
    def norm(self):
        pass