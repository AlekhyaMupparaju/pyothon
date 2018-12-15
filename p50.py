N=int(input())
K=0
for x in range(1,N+1):
    if(N%x==0):
        K=K+1
if(K!=0):
    print("yes")
else:
    print("no")
