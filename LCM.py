a,b=map(int,input().split())
Max=a if a > b else b
while(True) :
    if Max%a==0 and Max%b==0 :
        lcm=Max
        break
    Max+=1
print(lcm)