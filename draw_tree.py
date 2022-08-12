import nltk
from nltk.parse import RecursiveDescentParser

grammar1 = nltk.CFG.fromstring("""
S -> NP VP
VP -> V NP | V NP PP
PP -> P NP
V -> 'saw' | 'ate' | 'walked'
NP -> 'John' | 'Mary' | 'Bob' | Det N | Det N PP
Det -> 'a' | 'an' | 'the' | 'my'
N -> 'man' | 'dog' | 'cat' | 'telescope' | 'park'
P -> 'in' | 'on' | 'by' | 'with'
""")

grammar2 = nltk.CFG.fromstring("""
S -> NP VP
NP -> Det Nom | PropN
Nom -> Adj Nom | N
VP -> V Adj | V NP | V S | V NP PP
PP -> P NP
PropN -> 'Buster' | 'Chatterer' | 'Joe'
Det -> 'the' | 'a'
N -> 'bear' | 'squirrel' | 'tree' | 'fish'
Adj -> 'angry' | 'frightened' | 'little' | 'tall'
V -> 'chased' | 'said' | 'thought' | 'was' | 'put'
P -> 'on'
""") 

if __name__ == "__main__":
    rd1 = RecursiveDescentParser(grammar1)
    sentence1 = 'Mary ate a dog in a park'.split()
    sentence2 = 'John saw a man with telescope'.split()
    for t in rd1.parse(sentence1):
        print(t)
    