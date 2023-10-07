def make_key(str):          # returns the characters in string s in sorted order
    return ''.join(sorted(str))

def find_anagrams(words):   # returns a dict with keys and the words that match them
    anagrams = {}
    for word in words:
        anagrams.update({make_key(word): word})
    return anagrams

