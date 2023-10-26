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
    myquilt = pile(sew(a, reflect(a)), reflect(sew(a, reflect(a)), horizontal=True))
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
        for atom in row:
            if atom[0] == 'a':
                result += (string1[atom[1]])[:2]
            else:
                result += (string2[atom[1]])[:2]
        result += '\n'
        for atom in row:
            if atom[0] == 'a':
                result += (string1[atom[1]])[2:4]
            else:
                result += (string2[atom[1]])[2:4]
        result += '\n'
    return result

# Convenience Functions
def unturn(quilt):
    '''turns quilt once counterclockwise'''
    return turn(turn(turn(quilt)))

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
def pseudo_hilbert(n, quilt):
    '''returns an order n pseudo-hilbert curve using the specified quilt'''
    for i in range(n):
        quilt = sew(pile(quilt, turn(quilt)), pile(quilt, unturn(quilt)))
    return quilt

def reflect(quilt, horizontal = False):
    '''returns the mirror image of the quilt, defaulting to a vertical line of symmetry'''
    newQuilt = []
    if horizontal:
        for r in range(len(quilt)):
            newQuilt.append(quilt[len(quilt) - r - 1])
        return metamap(flip_hori, newQuilt)
    else:
        for row in quilt:
            newRow = []
            for c in range(len(quilt[0])):
                newRow.append(row[len(quilt[0]) - c - 1])
            newQuilt.append(newRow)
        return metamap(flip_vert, newQuilt)

def flip_vert(atom):
    '''flips an atom across a vertical line of symmetry'''
    if atom[1] % 2 == 0:
        return (atom[0], atom[1] + 1)
    return (atom[0], atom[1] - 1)

def flip_hori(atom):
    '''flips an atom across a horizontal line of symmetry'''
    return (atom[0], 3 - atom[1])
    

def checkerboard(quilt1, quilt2, m, n):
    '''returns a checkerboard pattern of quilts in a rectangle with m rows and n columns'''
    return

'''
graphics, when you get around to them :)

'''


main()