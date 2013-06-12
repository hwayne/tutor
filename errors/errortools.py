#Returns position, takes possible nesting into account 
def cut(tokenstream, tokenpos, cuttokens = ["RPAREN"], direction = 1, upstep = "LPAREN" , downstep = "RPAREN"):
    step = tokenstream[tokenpos] == upstep
    
    while True:

#Boundary values
        tokenpos += direction
        if tokenpos == len(tokenstream): return tokenpos
        elif tokenpos == -1: return tokenpos

        elem = tokenstream[tokenpos]
        if  elem == upstep: step += 1
        elif elem == downstep: step -= 1
        if elem in cuttokens and step == 0: return tokenpos

