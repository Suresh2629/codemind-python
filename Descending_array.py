n=int(input())
test_list=list(map(int,input().split()))
flag=0
i=1
while i<len(test_list):
    if(test_list[i]>test_list[i-1]):
        flag=1
    i+=1
if(not flag):
    print('yes')
else:
    print('no')