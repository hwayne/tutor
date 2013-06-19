from errors.errortools import cut
import tokens

class TokenTree():
    def __init__(self, tokenstring):
        self.tokentree = build_tree(tokenstring)

def flatten_tree(tree):
    if type(tree) == list: return tree
    else: return flatten_tree(tree[1])+[tree[0]]+flatten_tree(tree[2])

def is_tree(tree):
    ttype = type(tree)
    if ttype == list: return True #leaf
    elif ttype == tuple: #node
        if len(tree) != 3: return False
        elif tree[0] not in tokens.nodeops: return False
        else: return (is_tree(tree[1]) and is_tree(tree[2]))
    else: return False

# We walk through the string to get everything before and after an operator.
# Then, based on priority, we either make the operator balance on that or
# on the stuff before the next operator.

def build_tree(tokenstring):

#BEGIN 'WRAPPED IN PARENTHESIS' CASE
    if cut(tokenstring, 0, tokens.tokendict.values())+1 == len(tokenstring):
        inside = build_tree(tokenstring[1:-1])
        if type(inside) == list: #ie like (-1)
            return tokenstring
        else: return (inside[0], ['LPAREN']+inside[1], inside[2]+['RPAREN'])

    op_pos = cut(tokenstring, 0, tokens.ops)
#'NO OPERATOR' CASE
    if op_pos == len(tokenstring): #just numbers
        return tokenstring

    op = tokenstring[op_pos]

    next_op_pos = cut(tokenstring, op_pos, tokens.ops)
    branch1 = tokenstring[:op_pos]
    branch2 = tokenstring[op_pos+1:next_op_pos] #to skip the op

#'ONLY ONE OPERATOR' CASE
    if next_op_pos == len(tokenstring): #no next op
        return (op, build_tree(branch1), build_tree(branch2))

#ALL OTHER CASES
    next_op = tokenstring[next_op_pos]
    branch3 = tokenstring[next_op_pos+1:]
    if tokens.priority[next_op] <= tokens.priority[op]:
        return (next_op,
                (op, build_tree(branch1), build_tree(branch2)),
                build_tree(branch3))
    else:
        return (op,
                build_tree(branch1),
                (next_op, build_tree(branch2), build_tree(branch3)))

if __name__ == "__main__":

    L = Lexer()
    
    while True:
        tokenstream = L.lexString(raw_input())
        print build_tree(tokenstream)
