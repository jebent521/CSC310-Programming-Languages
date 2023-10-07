#1
def keep(arr, fun): return [i for i in arr if fun(i)]

#2
def make_key(str):          # returns the characters in string s in alphabetical order
    return ''.join(sorted(str))

def find_anagrams(words):   # returns a dict with keys and the words that match them
    anagrams = {}
    for word in words:
        dorw = make_key(word)
        if dorw in anagrams:
            anagrams[dorw] += [word]
        else:
            anagrams.update({dorw: [word]})
    return anagrams