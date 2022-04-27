import math
def perfect(n) :
    sq_rt=int(math.sqrt(n))
    if (sq_rt*sq_rt)==n :
        return True
    else :
        return False
n=int(input())
for i in range (n) :
    num=int(input())
    print(perfect(num))