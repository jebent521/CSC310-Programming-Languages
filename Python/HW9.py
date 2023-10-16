"""
1. The basic building block of a quilt is a tuple of the form ('a',2). The first element is the texture 'a' 
    or 'b' and the second element is the orientation 0,1,2,3 representing how many 90◦ clockwise
    rotations. Write a function turn_atom so that e.g. turn_atom(('a',2)) returns ('a',3) and
    turn_atom(('b',3)) returns ('b',0).

2. Write a higher order function called metamap given a function, f, and a list of lists, it should
    return a lists of lists with the function applied to all elements in the inner lists. For example, if
    square = lambda x: x*x and matrix = [[1,2,3],[4,5,6],[7,8,9]] then metamap(square, matrix)
    should return [[1,4,9],[16,25,36],[49,64,81]]. Furthermore, the body of your definition should be
    1 line long and should itself make use of map.

For the record, here is my own implementation of turn() in Little Quilt:

def turn(quilt):
    return metamap(turn_atom,rotate(quilt))

of course, to use it one would need to write rotate (which changes the location of the pieces but not
their orientation).
"""

def turn_atom(atom):
    return (atom[0], (atom[1] + 1) % 4)

def metamap(f, listOfRows):
    return [list(map(f, row)) for row in listOfRows]

print("Testing turn_atom()")
a = ('a', 0)
for i in range(5):
    print(a)
    a = turn_atom(a)

print("\nTesting metamap()")
matrix = [[1,2,3], [4,5,6], [7,8,9]]
newMatrix = metamap(lambda x: x*x, matrix)
for row in matrix:
    print (row)
print()
for row in newMatrix:
    print (row)