p=int(input())
l=list(map(int,input().split()))
n=[]
k=[]
res=[]
for i in l:
    if i%2==0:
        n.append(i)
    else:
        k.append(i)
res=n+k
for j in res:
    print(j,end=' ')