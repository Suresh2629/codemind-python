n=int(input())
a=0
b=1
temp=n
c=a+b
while c<n :
    a=b
    b=c
    c=a+b
if temp==0 :
    print("True")
if c==temp :
    print("True")
else :
    print("False")