n=int(input())
sum=1
temp=n
for i in range(2,n):
    if n%i==0:
        sum=sum+i
if sum > temp:
    print(True)
else:
    print(False)