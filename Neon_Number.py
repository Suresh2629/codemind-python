Number = int(input())
Sum = 0
sqr=Number*Number
while(sqr>0) :
    r=sqr%10
    Sum+=r
    sqr=sqr//10



if Sum == Number:
    print("Neon Number")
else:
    print("Not Neon Number")