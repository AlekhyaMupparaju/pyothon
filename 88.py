a,s=map(int,raw_input().split())
if(a>s):
    min1=a
else:
    min1=s
while(1):
    if(min1%a==0 and min1%s==0):
        print(min1)
        break
    min1=min1+1
