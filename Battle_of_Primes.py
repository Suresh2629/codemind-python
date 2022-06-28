def is_prime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return 0
    else:
        return 1
s=int(input())
e=int(input())
sum=0
summ=s+e
for i in range(1,50):
    sum=summ+i
    if(is_prime(sum)):
        print(i)
        break

