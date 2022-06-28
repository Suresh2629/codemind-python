n=int(input())
l=list(map(int,input().split()))
sum=0
k=int(input())
s=l.index(k)
for i in range(s+1):
    sum+=l[i]
print(sum)