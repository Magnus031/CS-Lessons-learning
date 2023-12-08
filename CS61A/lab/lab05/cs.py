def tree(root_label,branches=[]):
    #build a tree
    for branch in branches:
        assert is_tree(branch),'branch must be trees'
    return [root_label]+list(branches)

def is_tree(tree):
    #is_tree function is for verifying the tree if well-formed
    if type(tree)!=list or len(tree)<1:
        return False 
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True 

def branches(tree):
    return tree[1:]

def label(tree):
    return tree[0]    

def is_leaf(tree):
    return not branches(tree)

def fib_tree(n):
    '''build a nth Fibonacci tree 
    '''   
    if n==0 or n==1:
        return tree(n)
    else:
        left,right=fib_tree(n-2),fib_tree(n-1)
        fib_n=label(left)+label(right)
        return tree(fib_n,[left,right])
    
def count_leaves(tree):
    sum=0
    if is_leaf(tree):
        return 1
    else:
        for branch in branches(tree):
            sum+=count_leaves(branch)
    return sum

def partition_tree(n,m):
    '''return a partition tree of n using parts of up to m'''
    if n==0:
        return tree(True)
    elif n<0 or m==0:
        return tree(False)
    else:
        left,right=partition_tree(n-m,m),partition_tree(n,m-1)
        return tree(m,[left,right])

def print_parts(tree,partition=[]):
    if is_leaf(tree):
        if label(tree):
            print('+'.join(partition))
    else:
        left,right =branches(tree)
        m = str(label(tree))
        print_parts(left,partition+[m])
        print_parts(right,partition)

print_parts(partition_tree(2,2))
        