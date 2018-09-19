r,s=map(int,raw_input().split())
if r>s:
    c=r-s
else:
    c=s-r
if c%2==0:
    print "even"
else:
    print "odd"
