import math
s,m=map(int,raw_input().split())
a=s * m
if math.sqrt(a).is_integer():
    print "yes"
else:
    print "no"
