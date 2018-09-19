r,s=map(int,raw_input().split())
list=[int(x) for x in raw_input().split()]
if s in list:
    count=list.count(s)
    print count
else:
    print 0
