def isSum(a,b,c):
    if b<c:
        c,b=b,c
    while a>=0:
        if a%b==0:
            return True
        a-=c
    return False
        
a = int(input())
if isSum(a,3,7):
    print("yes")
else:
    print("no")
