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
from itertools import product
import typing

def main():
    myquilt=turn(sew(a, b))
    for row in myquilt:
        print(row)

a = [[('a', 0)]]
b = [[('b', 0)]]

def turn(quilt):
    newQuilt=[[None] * len(quilt)] * len(quilt[0])
    for i, j in product(range(len(quilt)), range(len(quilt[0]))):
        atom = (quilt[i][j])[0]
        orientation = ((quilt[i][j])[1] + 1) % 4
        newQuilt[j][i] = (atom, orientation)
    return newQuilt


def sew(quilt1, quilt2):
    newQuilt = []
    for i,j in zip(quilt1, quilt2):
        newQuilt.append(i + j)
    return newQuilt

def unturn(quilt):              # turns quilt once counterclockwise
    return turn(turn(turn(quilt)))

def pile(quilt1, quilt2):       # piles quilt1 on top of quilt2
    return unturn(sew(turn(quilt2), turn(quilt1)))

def pinwheel(quilt):
    pass

def repeat_block(quilt, m, n):
    pass

def quilt_to_string(quilt, string1, string2):
    pass

main()