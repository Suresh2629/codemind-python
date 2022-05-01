n=int(input())
e=0
o=0
m=0
while(n>0) :
    r=n%10
    m+=1
    if r%2==0 :
        e+=1
    elif r%2!=0 :
        o+=1

    n=n//10

if e==m :
    print("Even")
elif o==m :
    print("Odd")
else :
    print("Mixed")