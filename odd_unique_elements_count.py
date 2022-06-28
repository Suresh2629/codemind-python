n=int(input())
l=list(map(int,input().split()))
c=0
k=list(set(l))
for i in k:
    if i%2!=0:
        c+=1
print(c)
