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
from functools import reduce
# Main Method
def main():
    
    print('turn(a)')
    print(quilt_to_string(turn(a), a_pattern, b_pattern))
    print('sew(a, b)')
    print(quilt_to_string(sew(a,b), a_pattern, b_pattern))
    print('unturn(a)')
    print(quilt_to_string(unturn(a), a_pattern, b_pattern))
    print('pile(a, b)')
    print(quilt_to_string(pile(a,b), a_pattern, b_pattern))
    print('pinwheel(a)')
    print(quilt_to_string(pinwheel(a), a_pattern, b_pattern))
    print('repeat_block(a, 3 , 3)')
    print(quilt_to_string(repeat_block(a,3,3), a_pattern, b_pattern))
    print('reflect(a)')
    print(quilt_to_string(reflect(a), a_pattern, b_pattern))
    print('reflect(a, horizontal=True)')
    print(quilt_to_string(reflect(a, horizontal=True), a_pattern, b_pattern))
    print('checkerboard(a, b, 3, 3)')
    print(quilt_to_string(checkerboard(a,b,3,3), a_pattern, b_pattern))
    print('pseudo_hilbert(3, a)')
    print(quilt_to_string(pseudo_hilbert(3,a), h1_pattern, h2_pattern))
    print('Something that might actually resemble a quilt:')
    myquilt = pinwheel(pile(pile(reduce(sew, [pinwheel(a), repeat_block(pinwheel(turn(b)), 1, 3), pinwheel(a)]), repeat_block(pinwheel(turn(b)), 3, 5)), reduce(sew, [pinwheel(a), repeat_block(pinwheel(turn(b)), 1, 3), pinwheel(a)])))
    print(quilt_to_string(myquilt, a_pattern, b_pattern))


# Defining Quilt Atoms
a = [[('a', 0)]]
b = [[('b', 0)]]
a_pattern = ['┌─│┌', '─┐┐│', '┘│─┘', '│└└─']
b_pattern = ['╭─│╭', '─╮╮│', '╯│─╯', '│╰╰─']
h1_pattern = ['┌┐││', '─┐─┘', '││└┘', '┌─└─']
h2_pattern = ['╭╮││', '─╮─╯', '││╰╯', '╭─╰─']

# Turn Function (uses turn_atom, metamap, and rotate)
def turn_atom(atom):
    '''turns an individual quilt atom (tuple) by incrementing its orientation'''
    return (atom[0], (atom[1] + 1) % 4)

def metamap(f, quilt):
    '''maps the function f over the 2D array quilt'''
    return [list(map(f, row)) for row in quilt]

def rotate(quilt):
    '''rotates the elements in a 2D array quilt 90 degrees clockwise (but doesn't change the atoms' orientations)'''
    newQuilt = []                               # create new quilt
    maxC = len(quilt) - 1                       # number of rows in old quilt becomes number of columns in new quilt (-1 for indexing)
    for r in range(len(quilt[0])):              # for each new row (number of new rows = number old columns)
        newRow = []                             # create new row
        for c in range(len(quilt)):             # for each new column
            newRow.append(quilt[maxC - c][r])       # append atom to new row
        newQuilt.append(newRow)                 # append new row to new quilt
    return newQuilt

def turn(quilt):
    '''turns a quilt 90 degrees clockwise'''
    return metamap(turn_atom, rotate(quilt))

# Sew Function: sews quilt2 to the right of quilt1
def sew(quilt1, quilt2):
    '''sews quilt2 to the right of quilt1'''
    if len(quilt1) != len(quilt2):              # ensure quilts are the same height
        raise Exception("Quilts aren't the same height!")
    newQuilt = []
    for i,j in zip(quilt1, quilt2):             # pair corresponding rows in quilts 1 and 2
        newQuilt.append(i + j)                  # concatenate them and append to new quilt
    return newQuilt

# Quilt To String Function: returns a stringified quilt
def quilt_to_string(quilt, string1, string2):
    '''returns a stringified quilt using string1 for 'a' atoms and string2 for 'b' atoms'''
    result = ''
    for row in quilt:
        for atom in row:                        # iterate through each atom in the row, printing the first 2 characters
            if atom[0] == 'a':
                result += (string1[atom[1]])[:2]
            else:
                result += (string2[atom[1]])[:2]
        result += '\n'
        for atom in row:                        # iterate through each atom in the row, printing the last 2 characters
            if atom[0] == 'a':
                result += (string1[atom[1]])[2:4]
            else:
                result += (string2[atom[1]])[2:4]
        result += '\n'
    return result

# Convenience Functions
def unturn(quilt):
    '''turns quilt once counterclockwise'''
    return turn(turn(turn(quilt)))      # equal to 3 turns

def pile(quilt1, quilt2):
    '''piles quilt1 on top of quilt2'''
    return unturn(sew(turn(quilt2), turn(quilt1)))

def pinwheel(quilt):
    '''going clockwise starting at the top left, it returns a square of quilts where each next quilt is rotated'''
    return sew(pile(quilt, unturn(quilt)), pile(turn(quilt), turn(turn(quilt))))

def repeat_block(quilt, m, n):
    '''repeats quilt in a grid of m rows and n columns'''
    result = quilt
    for i in range(m-1):                # get a column of quilts m rows high
        result = pile(result, quilt)
    quilt = result
    for i in range(n-1):                # widen the quilts n columns wide
        result = sew(result, quilt)
    return result

# Extra Credit Functions 
def reflect(quilt, horizontal = False):
    '''returns the mirror image of the quilt, defaulting to a vertical line of symmetry'''
    newQuilt = []
    if horizontal:                  # reflecting down over a horizontal line of symmetry
        return unturn(reflect(turn(quilt)))
    else:                           # reflecting right over a vertical line of symmetry
        for row in quilt:
            newRow = []
            for c in range(len(quilt[0])):  # append each column in reverse order
                newRow.append(row[len(quilt[0]) - c - 1])
            newQuilt.append(newRow)
        return metamap(flip, newQuilt)

def flip(atom):
    '''flips an atom across a vertical line of symmetry'''
    if atom[1] % 2 == 0:
        return (atom[0], atom[1] + 1)
    return (atom[0], atom[1] - 1)

def checkerboard(quilt1, quilt2, m, n):
    '''returns a checkerboard pattern of quilts in a rectangle with m rows and n columns'''
    newQuilt = quilt1                       # define first row (need something to pile the rest onto)
    for c in range(1, n):                   # sew quilt1 and quilt2 onto it, alternating
        if c % 2 == 0:
            newQuilt = sew(newQuilt, quilt1)
        else:
            newQuilt = sew(newQuilt, quilt2)
    for r in range(1, m):                   # add on subsequent rows
        if r % 2 == 0:                      # first quilt in each row alternates
            newRow = quilt1
        else:
            newRow = quilt2
        for c in range(1, n):               # sew quilt1 and quilt2 onto newRow, alternating
            if r % 2 == c % 2:
                newRow = sew(newRow, quilt1)
            else:
                newRow = sew(newRow, quilt2)
        newQuilt = pile(newQuilt, newRow)   # pile newRow under newQuilt
    return newQuilt

def pseudo_hilbert(n, quilt):
    '''returns an order n pseudo-hilbert curve using the specified quilt'''
    for i in range(n):
        quilt = sew(pile(quilt, turn(quilt)), pile(quilt, unturn(quilt)))
    return quilt
'''It's not a very good-looking hilbert curve but that's because of the limitations
of using only one quilt with no connecting bits. You can sort of follow the pattern, though.
It always starts at the bottom-left corner, and you can trace the path the hilbert curve would
take if you know what a hilbert curve looks like.'''

main()