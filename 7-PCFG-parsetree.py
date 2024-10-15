from nltk import PCFG, InsideChartParser
grammar = PCFG.fromstring("""
S -> NP VP [1.0]
NP -> NP PP [0.4] | 'he' [0.1] | 'dessert' [0.3] | 'lunch' [0.1] | 'saw' [0.1]
PP -> Pre NP [1.0]
VP -> Verb NP [0.3] | VP PP [0.7]
Pre -> 'with' [0.6] | 'in' [0.4]
Verb -> 'ate' [0.7] | 'saw' [0.3]
""")
parser = InsideChartParser(grammar)
tokens = "he saw lunch with dessert".split()
for tree in parser.parse(tokens):
    tree.pretty_print()
    print("PROBABILITY: ",tree.prob())
    #tree.draw()