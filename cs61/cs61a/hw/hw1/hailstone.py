def hailstone(x):
    #num is the number of step
    num=1
    while x>1:
        print(x)
        if x%2==0:
            x//=2
        else :
            x=3*x+1
        num+=1
    print(1)
    return num
a=hailstone(10)
print(a)