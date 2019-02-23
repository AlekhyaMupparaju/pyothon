def sumpair(l,n,c):
    for i in range(l):
        for j in range(i+1,l):
            if ((c[i]+c[j])==n):
                return('yes')
n=(input()).split()
n=list(map(int,n))
m=(input()).split()
m=list(map(int,m))
print(sumpair(n[0],n[1],m))                   
    
