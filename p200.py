import sys, string, math

S = raw_input()
l = []
for c in S :
    if c not in l :
        l.append(c)
S2 = ''.join(l)
print(S2)
