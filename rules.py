# stores each rule as a tuple pair, with the first item
# storing the phrase type, and the second as the
# list of the atoms that compose it
NP1 = ("NP", ["D", "N"])
NP2 = ("NP", ["D", "Adj", "N"])
PP = ("PP", ["P", NP1])
VP = ("VP", ["V", "Adv", PP])
S = ("S", [NP1, VP])