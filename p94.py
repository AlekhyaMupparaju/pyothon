import sys,string, math,itertools
N = raw_input()
for d in N :
    if N.count(d) > 1 :
        print('yes')
        sys.exit()
print('no')
