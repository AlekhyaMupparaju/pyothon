y=int(raw_input())
reverse=0
while(y>0):
    remainder=y%10
    reverse=reverse*10+remainder
    y=y/10
print reverse  
