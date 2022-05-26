t=int(input())
for k in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    if n==0:
        print(0)
    else:
        v=[]
        for i in arr:
          if i in range(1,1000000000,2):
                v.append(i)
        if len(v)==1:
            print(0)
        elif len(v)%2==0:
            print(len(v)//2)
        else:
            print((len(v)-1)//2)