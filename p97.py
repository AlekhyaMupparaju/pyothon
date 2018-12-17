import sys,string, math,itertools
N,k = raw_input().split()
N,k = int(N),int(k)
sum1 = 0
for i in range(N,k+1) :
    if i%2==1 :
        sum1 += i
print(sum1)
