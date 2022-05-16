n,x=map(int,input().split())
l=len(str(n))
last=n%(10**x)
while(l!=x):
    n=n//10
    l-=1
first=n
print(abs(first-last))