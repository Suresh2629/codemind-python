def is_prime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return 0
    else:
        return 1
n=int(input())
c=1
for i in range(1,n+1):
    if(is_prime(i)==0):
        if(n%i==0):
            c+=1
print(c)