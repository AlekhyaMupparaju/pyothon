n,k=map(int,raw_input().split())
p=int(n/2)
q=int(k**0.5)
if(p*2==n and q*q==k):
    print("yes")
else:
    print("no")
