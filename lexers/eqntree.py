from errors.errortools import cut
import tokens

def flattenTree(tree):
    if type(tree) == list: return tree
    else: return flattenTree(tree[1])+[tree[0]]+flattenTree(tree[2])

def isTree(tree):
    ttype = type(tree)
    if ttype == list: return True #leaf
    elif ttype == tuple: #node
        if len(tree) != 3: return False
        elif tree[0] not in tokens.ops: return False
        else: return (isTree(tree[1]) and isTree(tree[2]))
    else: return False
