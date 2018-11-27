c,d=map(int,raw_input().split())
def gcd(a,s):
    z=abs(a-s)
    if (a-s)==0:
        return s
    else:
        return gcd(z,min(a,s))
print gcd(c,d)
