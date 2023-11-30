"""
Jonah Ebent, CSC310 Programming Languages, enzymes.py, 12/1/23
1. Write a function called seq2re() that takes a recognition sequence, strips away everything which
    isn't a letter or a comma, replaces the ambiguity codes by character classes according to the
    table below (and leaves A,T,C,G alone) and replaces any comma by |.
2. Takes the dictionary enz2seq from the file enzymes.py and transforms it into a dictionary enz2re
    mapping enzymes to regular expressions (discarding any for which the recognition is unknown).
    Note that this is essentially a filter+map.
3. Write a function called find_enzymes(strand) which will take a strand of DNA (a string in 'ATGC')
    and iterates over the dictionary, grabbing all enzymes (keys) for which the corresponding
    regular expression matches something in the strand. For a moderately large strand the number
    of hits can be quite large, so in testing it you might want to assign it to a variable. re.search()
    might help.
"""

import re

# 1
def seq2re(seq):
    replacements = {'R': '[GA]',
                    'Y': '[CT]',
                    'M': '[AC]',
                    'K': '[GT]',
                    'S': '[GC]',
                    'W': '[AT]',
                    'B': '[CGT]',
                    'D': '[AGT]',
                    'H': '[ACT]',
                    'V': '[ACG]',
                    'N': '[ACGT]',
                    ',': '|'}
    regex = r''
    for char in seq:
        if char in ['A', 'C', 'G', 'T']:
            regex += char
        elif char in replacements.keys():
            regex += replacements[char]
    return regex

# 3
def find_enzymes(strand):
    enzymes = []
    for enz, seq in enz2re.items():
        if isinstance(re.search(seq, strand), re.Match):
            enzymes.append(enz)
    return enzymes

pat = r'^<1>(.*)\n(?:.*\n){3}<5>(.*)$'
my_re = re.compile(pat, flags=re.M)

with open("link_allenz.txt") as f:
    s = f.read()

hits = my_re.findall(s)
enz2seq = dict(hits)

# 2
enz2re = {i:seq2re(j) for i,j in enz2seq.items() if len(seq2re(j)) != 0}