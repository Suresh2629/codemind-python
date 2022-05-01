n=int(input())
if n>=3 :
    for i in range (1,n+1) :
        for j in range (1,i+1) :
            print("*",end='')
        print()
    for i in range (n,1,-1) :
        for j in range (1,i):
            print("*",end='')
        print()
else :
    print('The pattern is not possible')