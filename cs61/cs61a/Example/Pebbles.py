def play_Alice(n):
    if n==0:
        print('Bob Wins!') 
    else:
         play_Bob(n-1)
    
def play_Bob(n):
    if  n==0:
        print('Alice wins!')
    else:
        if n%2==0:
             play_Alice(n-2)
        elif n%2==1:
             play_Alice(n-1)

play_Alice(20)