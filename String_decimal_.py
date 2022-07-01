t=int(input())
for i in range(t):
    a=input()
    f=0
    for j in a:
        if j.isdigit():
            f=1
        else:
            f=0
            break
    if f==1:
        print("True")
    else:
        print("False")