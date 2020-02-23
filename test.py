
A=[-1,-3]

def solution(X):
    # write your code in Python 3.6
    y=1
    for n in A:
        if n>0 and y!=n:      
            print(y)
            break           
        if n<0:
            y=1
            print(y)
            break
        if n>0 and y==n:
            if y==X[-1]:
                print(y+1)
            y=y+1
    
    pass

solution(A)
