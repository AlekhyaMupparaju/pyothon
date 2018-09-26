s=int(raw_input())
count=0
if s>0:
    for i in range(1,s+1):
        if s%i==0:
            print i,
