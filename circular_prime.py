n=int(input())
flag=0
count=0
rev=0
if n>1:
    for i in range (2,n):
        if n%i==0:
            flag=1
while n>0:
    r=n%10
    rev=rev*10+r
    n=n//10
temp=rev
if temp>=1:
    for i in range (2,temp):
        if temp%i==0:
            count=1
    if flag==1 and count==1:
        print("not prime")
    elif flag==0 and count==1:
        print("prime but not a circular prime")
    else:
        print("circular prime")
    