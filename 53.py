a=int(raw_input())
s=[]
while(a>0):
    dig=a%10
    s.append(dig)
    a=a//10
print sum(s)
