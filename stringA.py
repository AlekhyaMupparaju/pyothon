A=str(raw_input())
for x in range(1,len(A)):
    if A[x:]>A:
        print(A[x:])
        break
