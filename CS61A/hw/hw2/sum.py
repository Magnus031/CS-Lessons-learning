def summation(n,term):
    k=1
    sum=0
    while k<=n:
        sum,k=sum+term(k),k+1
    return sum

def cube(x):
    return x**3
p=summation(3,cube)
print(p)