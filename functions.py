import lexicon as l
import rules as r
import random

# generates a string representation of a given syntactic rule
def syntaxtree(rule: tuple, depth=0):
    label = rule[0]
    children = rule[1]
    indent = "     "
    output = ""
    
    output += indent*depth + "(" + label + "\n"
    for child in children:
        if isinstance(child, tuple):
            output += syntaxtree(child, depth+1) + "\n"
        else:
            output += indent*(depth+1) + child + "\n"
    output += indent*depth + ")"
    return output

# print syntaxtree
def pst(rule:tuple):
    print(syntaxtree(rule))

# identical to syntaxtree() but now includes a random word
# taken from the lexicon next to each terminal node
def wordtree(rule: tuple, depth=0):
    label = rule[0]
    children = rule[1]
    indent = "     "
    output = ""
    output += indent*depth + "(" + label + "\n"
    for child in children:
        if isinstance(child, tuple):
            output += wordtree(child, depth+1) + "\n"
        else:
            word = random.choice(l.lex[child])
            output += indent*(depth+1) + child + " " + word + "\n"
    output += indent*depth + ")" 
    return output

# print wordtree
def pwt(rule: tuple):
    print(wordtree(rule))

# generate sentence
def gen_sen(rule: tuple):
    children = rule[1]
    sentence = ""
    for child in children:
        if isinstance(child, tuple):
            sentence += gen_sen(child)
        else:
            word = random.choice(l.lex[child])
            sentence += word + " "
    return sentence

# print sentence
def pr_sen(rule: tuple):
    print(gen_sen(rule))

# generate sentence with bracket structure
def gen_brac(rule: tuple):
    label = rule[0]
    children = rule[1]
    output = []
    for child in children:
        if isinstance(child, tuple):
            output.append([child[0], gen_brac(child)])
        else:
            word = random.choice(l.lex[child])
            output.append([child, word])
    return output

# print sentence with bracket structure
def pr_brac(rule: tuple):
    print(gen_brac(rule))

