a=int(raw_input())
count=0
if a>1:
    for i in range(2,a):
        if a%i==0:
            count=count+1
if count>1:
    print "yes"
else:
    print "no"
