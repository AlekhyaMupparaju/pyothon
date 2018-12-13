n,k,p=map(int,raw_input().split())
if(n+k<=p or k+p<=n or p+n<=k):
    print "no"
else:
    print "yes"
