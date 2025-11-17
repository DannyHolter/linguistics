import lexicon as l
import rules as r
import random

lex = l.lex
form = r.S

def syntaxtree(rule, depth=0):
    label = rule[0]
    children = rule[1]
    print("     "*depth + "(" + str(label))
    for child in children:
        if isinstance(child, tuple):
            syntaxtree(child, depth+1)
        else:
            print("     "*(depth+1) + child)
    print("     "*depth +")")

def wordtree(rule, depth=0):
    label = rule[0]
    children = rule[1]
    print("     "*depth + "(" + str(label))
    for child in children:
        if isinstance(child, tuple):
            wordtree(child, depth+1)
        else:
            print("     "*(depth+1) + child + " " + str(random.choice(lex[child])))
    print("     "*depth +")")