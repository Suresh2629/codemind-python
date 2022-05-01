n=int(input())
rem=0
r=0
rev=0
rev2=0
square = n * n

while n > 0 : 
    rem = n % 10
    rev = rev * 10 + rem
    n = n // 10
    
square2 = rev * rev

while square2 > 0 :
    r = square2 % 10
    rev2 = rev2 * 10 + r
    square2 = square2 // 10
        
if square == rev2 :
    print("True")
else :
    print("False")