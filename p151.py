import sys,string, math,itertools
N = input()
k = len(N) - N.count('a') -N.count('b')
if k <= 1 :
    print('yes')
else :
    print('no')


