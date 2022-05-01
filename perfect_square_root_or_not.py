n=int(input())
flag=0
for i in range (1,n) :
    if i*i == n :
        flag=1
if flag :
    print("True")
else :
    print("False")