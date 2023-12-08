from math import sqrt
phi=1/2+sqrt(5)+1#二分之根号五加1
def improve(update,close,guess=1):
    while not close(guess):
        guess=update(guess)
    return guess

def update(x):
    return 1+1/x

def approx_eq(a,b,tolerance=1e-3):
    return abs(a-b)<tolerance

def close(a):
    return approx_eq(a**2,a+1)
def goldtest():#user_function ,which to test the answer if the expected result by using the assert function
    p=improve(update,close,guess=1)
    assert(approx_eq(p,phi)), 'p is the equal of gold ratio'
goldtest()    
