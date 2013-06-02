import tokens
from copy import copy

#For testing purposes
def identity(problem):
    return problem

#Returns positions in the token list used
def tokencut(tokenstream, tokenpos, cutpoints):
    lpos = tokenpos-1
    rpos = tokenpos+1
    while tokenstream[lpos] not in cutpoints and lpos+1 != 0:
        lpos -= 1
    while rpos != len(tokenstream) and tokenstream[rpos] not in cutpoints: 
        rpos += 1
    return (lpos,rpos)

#Looks through problem, returns varients that replace (first) operator
#Currently can't make multiple changes, IE 1+2+3 -> 1*2-3

def operror(problem): #:: tokenlist -> [tokenlist]
    newproblems = []
    for pos, elem in enumerate(problem):
        if elem in tokens.ops:
            for op in tokens.ops:
                temp = copy(problem)
                temp[pos] = op
                newproblems.append((temp, "wrong operator"))

    return newproblems

#We walk backwards through the problem, tight binding around every minus operator
#Also binds returns non-errors (ie replacing 2+2*2 with 2+(2*2)), but these are dropped for as they give correct answers

def assocerror(problem):
    newproblems = []
    for pos in range(len(problem))[::-1]:
        if problem[pos] in tokens.ops :
            (x,y) = tokencut(problem, pos, tokens.ops)
            temp = copy(problem)
            temp.insert(y, "RPAREN") #Goes before operator
            temp.insert(x+1, "LPAREN") #Goes after operator. After RPAREN to not screw up order
            newproblems.append((temp, "wrong order of operations"))
            pos = x+1
    return newproblems
    
#Create space of all possible negative removals
def negerror(problem):
    newproblems = []
    for pos, elem in enumerate(problem):
        if elem == "NEG":
            temp = copy(problem)
            temp.pop(pos)
            newproblems.append((temp,"dropped negative sign"))
            newproblems += negerror(temp) #Recursive, get all space
    return newproblems

