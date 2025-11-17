import lexicon as l
import rules as r
import random

lex = l.lex
form = r.S
def generate(stuff):
    for item in stuff:
        if not isinstance(item, list):
            print(item)
        else:
            generate(item)

def syntaxtree(rule, depth=0):
    print("     "*depth + "(" + str(rule[0]))
    for child in rule[1]:
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
            if isinstance(child, str):
                print("     "*(depth+1) + child + " " + str(random.choice(lex[child])))
            else:
                print("     "*(depth+1) + child)
    print("     "*depth +")")

wordtree(form)