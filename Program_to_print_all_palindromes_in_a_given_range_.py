s=int(input())
e=int(input())
for i in range(s,e+1):
    temp=i
    tempdup=temp
    r=0
    while i:
        rem=i%10
        r=r*10+rem
        i=i//10
    if tempdup==r:
        print(tempdup,end=' ')
    
        