N=int(raw_input())
x=N
k=[]
while (N>0):
    a=int(float(N%2))
    k.append(a)
    N=(N-a)/2
string=""
for j in k[::-1]:
    string=string+str(j)
print string
