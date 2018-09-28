s=int(raw_input())
b=[]
while s!=0:
    c=s%10
    if c%2==1:
        b.append(c)
    s=s/10
print str(b[::-1]).replace('[',"").replace(']',"")
