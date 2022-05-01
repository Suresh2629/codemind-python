m,n=map(int,input().split())
hcf=1
min=n if m>n else m
for i in range (1,min+1) :
    if(m%i==0 and n%i==0) :
        hcf=i
print(hcf)