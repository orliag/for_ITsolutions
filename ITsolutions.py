def digits(value):
    k=0
    while value>0:
        value = value // 10
        k += 1
    return k


n = int(input())
t=0
i=0  
while (True):
    if(t>=n):
        break
    i+=1
    
    if(i%digits(i)==0):
        t+=1
        print (i, end=" ")
