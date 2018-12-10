a=int(input())
sum=0
while(a>0):
    n=int(a%10)
    sum=(n*n)+sum
    a=int(a/10)
print(sum)
