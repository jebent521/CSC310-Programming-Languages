"""
Jonah Ebent, 10/27/23, CSC310 Programming Languages, LittleQuilt.py
This is an implementation of Sethi's Little Quilt, a toy language for defining quilts.

A quilt is a list of rows, all of which need to have the same length.
    For example,
        [[("a",1), ("a",0), ("b",1)], 
        [("b",2), ("a",1), ("a", 3)]]
    is a 2x3 quilt.
A row is a list of oriented atoms.
An oriented atom is a tuple of the form ("q",i) where "q" is a quilt atom and i is an integer in the range 0,1,2,3.
    ("q", i) represents "q" rotated clockwise through i clockwise 90 degree rotations.
A quilt atom will be a single letter either "a" or "b".
"""
# Main Method
def main():
    #myquilt=pseudo_hilbert(3, a)
    #for row in myquilt:
    #    print(row)
    myquilt = pile(sew(a, turn(b)), sew(unturn(b), turn(turn(a))))
    for row in myquilt:
        print(row)
    
    #print(quilt_to_string(myquilt, a_pattern, b_pattern))

# Defining Quilt Atoms
a = [[('a', 0)]]
b = [[('b', 0)]]
a_pattern = ['┌─\n│┌', '─┐\n┐│', '┘│\n─┘', '│└\n└─']
b_pattern = ['╭─\n│╭', '─╮\n╮│', '╯│\n─╯', '│╰\n╰─']

# Turn Function (uses turn_atom, metamap, and rotate)
def turn_atom(atom):
    return (atom[0], (atom[1] + 1) % 4)

def metamap(f, quilt):
    return [list(map(f, row)) for row in quilt]

def rotate(quilt):
    newQuilt = []
    maxC = len(quilt) - 1
    for r in range(len(quilt[0])):
        newRow = []
        for c in range(len(quilt)):
            newRow.append(quilt[maxC - c][r])
        newQuilt.append(newRow)
    return newQuilt

def turn(quilt):
    return metamap(turn_atom, rotate(quilt))

# Sew Function: sews quilt2 to the right of quilt1
def sew(quilt1, quilt2):
    newQuilt = []
    for i,j in zip(quilt1, quilt2):
        newQuilt.append(i + j)
    return newQuilt

# Quilt To String Function: returns a stringified quilt
def quilt_to_string(quilt, string1, string2):
    result = ''
    for row in quilt:
        for atom in row:
            if atom[0] == 'a':
                result += string1[atom[1]]
            else:
                result += string2[atom[1]]
        result += '\n'
    return result

# Extra (Convenience) Functions
def unturn(quilt):              # turns quilt once counterclockwise
    return turn(turn(turn(quilt)))

def pile(quilt1, quilt2):       # piles quilt2 on top of quilt1
    return unturn(sew(turn(quilt1), turn(quilt2)))

def pinwheel(quilt):
    pass

def repeat_block(quilt, m, n):
    pass

def pseudo_hilbert(n, quilt):
    for i in range(n):
        quilt = sew(pile(turn(quilt), quilt), pile(unturn(quilt), quilt))
    return quilt

main()