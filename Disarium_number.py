n=int(input())
length=len(str(n))
c=0
sum=0
temp=n
while(n):
    rem=n%10
    sum=sum+int(rem**length)
    n=n//10
    length=length-1
if sum==temp:
    print(True)
else:
    print(False)
    