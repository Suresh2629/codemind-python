Number = int(input())
Temp = Number
Sum = 0
prod = 1

while Temp > 0:
    lastDigit = Temp % 10
    Sum = Sum + lastDigit
    prod = prod * lastDigit
    Temp = Temp // 10


if Sum == prod:
    print("Spy Number")
else:
    print("Not Spy Number")