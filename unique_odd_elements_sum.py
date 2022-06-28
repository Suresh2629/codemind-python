n=int(input())
test_list=list(map(int,input().split()))
sum=0
k=list(set(test_list))
for i in k:
    if i%2!=0:
        sum+=i
print(sum)
