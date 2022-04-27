n=int(input())
temp=n
Sum=0
prod=1
while(temp>0) :
    r=temp%10
    Sum+=r
    prod*=r
    temp=temp//10
r=prod-Sum
print(r)