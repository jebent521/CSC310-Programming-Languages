#new_quilt.py (written by Dr. Coleman, modified by Jonah Ebent)

def rotate_matrix(mat):
    return [list(reversed(column)) for column in zip(*mat)]

#I never used the next two functions

def sew(mat1,mat2):
    return [row1+row2 for row1,row2 in zip(mat1,mat2)]

def pile(mat1,mat2):
    return [row.copy() for row in mat1 + mat2]

def rotate_string(s,rot_table = None):
    if rot_table:
        s = s.translate(rot_table)
    chars = [list(row) for row in s.split('\n')]
    chars = rotate_matrix(chars)
    return '\n'.join(''.join(row) for row in chars)

#candidates for a_string and b_string:

##a_string = ' \u1403 \n\u140Ax\u1405\n \u1403 '
##a_table = str.maketrans('\u1401\u1403\u1405\u140A','\u140A\u1405\u1401\u1403')
##b_string = ' \u1570 \n\u1572O\u1573\n \u1570 '
##b_table = str.maketrans('\u1570\u1571\u1572\u1573','\u1573\u1572\u1570\u1571')

a_string = '\u25F3\u25F3\u25F3\n\u25A3\u25A3\u25F3\n\u25A3\u25A3\u25F3'
a_table = str.maketrans('\u25F0\u25F1\u25F2\u25F3','\u25F3\u25F0\u25F1\u25F2')
b_string = '\u25A4\u25A4\u25A4\n\u25A3\u25A4\u25A4\n\u25A3\u25A3\u25A4'
b_table = str.maketrans('\u25A4\u25A5','\u25A5\u25A4')

def test_string(s,t = None):
    for i in range(4):
        print(s)
        print('')
        s = rotate_string(s,t)

#test_string(b_string,b_table)

class Piece:
    def __init__(self,texture, orientation, piece_string,piece_table = None):
        self.texture = texture
        self.orientation = orientation
        self.string = piece_string
        self.table = piece_table

    def __repr__(self):
        return f'Piece({self.texture},{self.orientation}, ...)'

    def __str__(self):
        return self.string

    def copy(self):
        return Piece(self.texture, self.orientation,self.string,self.table)

    def rotate(self,n):
        n = n % 4
        new_string = self.string
        for _ in range(n):
            new_string = rotate_string(new_string,self.table)
        return Piece(self.texture,(self.orientation + n) % 4,new_string,self.table)

class Quilt:
    def __init__(self,description):
        a = Piece('a',0,a_string,a_table)
        b = Piece('b',0,b_string,b_table)
        pieces = {'a':a,'b':b}
        self.description = description
        self.quilt = []
        for line in description.split('\n'):
            row = []
            items = line.split(',')
            for item in items:
                texture, orientation = item
                orientation = int(orientation)
                row.append(pieces[texture].rotate(orientation))
            self.quilt.append(row)

    def __repr__(self):
        hex_address = '0x'+hex(id(self))[2:].zfill(16).upper()
        return f'<Quilt object at {hex_address}>'

    def __str__(self):
        rows = []
        for row in self.quilt:
            subrows = [p.string.split('\n') for p in row]
            rows.append('\n'.join(''.join(pieces) for pieces in zip(*subrows)))
        return '\n'.join(rows)

    def __add__(self,other):        # equivalent to sew
        if len(self.quilt) != len(other.quilt):
            raise ValueError('Can only sew quilts of same height')
        d1 = self.description
        d2 = other.description
        d = '\n'.join(row1 + ',' + row2 for row1,row2 in zip(d1.split('\n'),d2.split('\n')))
        return Quilt(d)

    def __iadd__(self,other):
        if len(self.quilt) != len(other.quilt):
            raise ValueError('Can only sew quilts of same height')
        return self + other

    def __truediv__(self,other):    # equivalent to pile
        if len(self.quilt[0]) != len(other.quilt[0]):
            raise ValueError('Can only pile quilts of same width')
        d1 = self.description
        d2 = other.description
        d = d1 +'\n' + d2
        return Quilt(d)

    def __pow__(self,r):            # equivalent to rotate
        if not isinstance(r,int):
            raise TypeError(f"unsupported operand type(s) for **: 'Quilt' and '{type(other).__name__}'")
        r = r%4
        pieces = [row.split(',') for row in self.description.split('\n')]
        for _ in range(r):
            pieces = rotate_matrix(pieces)
        for i in range(len(pieces)):
            for j in range(len(pieces[0])):
                t,k = pieces[i][j]
                k = str((int(k)+r) % 4)
                pieces[i][j] = t + k
        description = '\n'.join(','.join(row) for row in pieces)
        return Quilt(description)

a = Quilt('a0')
b = Quilt('b0')

#Test

c = (a+b)/(b+a)
print(a)
print(b)
print(c)
print((c + c**1 + c**2 + c**3)/(c**3 + c**2 + c**1 + c))


    
                
        
    
        

    
    

