def largest_factor(x):
    for i in range(x//2,0,-1):
        if x % i ==0:
            return i

q=largest_factor(80)
print(q)
