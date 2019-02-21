m,s=map(int,(raw_input()).split())
a= []
(p,q) = ([],[])
a = list(map(int,(raw_input()).split()))
if(m%2!=0):
    p=a[:m-1]
    q=a[m-1:m]
else:
    p=a[:m//2]
    q=a[m//2:m]
print(max(min(p),min(q)))
