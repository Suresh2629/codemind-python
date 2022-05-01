n1=int(input())
n2=int(input())
Sumn1=0
Sumn2=0
d=0
for i in range (1,n1) :
    if n1%i==0 :
        Sumn1=Sumn1+i
for j in range (1,n2) :
    if n2%j==0 :
        Sumn2=Sumn2+j
if (Sumn1==n2 and Sumn2==n1) :
    print("Amicable")
else :
    print("Not Amicable")