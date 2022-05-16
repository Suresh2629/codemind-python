n=int(input())
for i in range(n,1,-1):
    for j in range(2,int(i**0.5)+1):
        if i%j==0:
            break
    else:
        temp=i
        break
b=n
while True:
    for j in range(2,int(n**0.5)+1):
        if n%j==0:
            break
    else:
        temp1=n
        break
    n+=1
res=abs(b-temp)
res1=abs(b-temp1)
if res<=res1:
    print(res)
else:
    print(res1)
    
        