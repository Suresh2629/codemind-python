t,s,b=map(int,input().split())
T=2*s*t*b*512
res=T//1024
print('{}KB'.format(res))