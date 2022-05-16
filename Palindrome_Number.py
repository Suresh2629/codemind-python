def palindrome(a):
    temp=a
    rev=0
    while(a):
        rem=a%10
        rev=rev*10+rem
        a=a//10
    if temp == rev:
        return True
    else:
        return False
n=int(input())
while n>0:
    a=int(input())
    if palindrome(a):
        print('True')
    else:
        print('False')
    n-=1
        
        
