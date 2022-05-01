n=int(input())
flag=0
if n > 1 :
    for i in range(2,n) :
        if n%i==0 :
            flag=1
if flag :
    print("not a prime")
else :
    print("prime")