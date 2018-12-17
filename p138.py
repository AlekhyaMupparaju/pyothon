N=int(raw_input())
print("yes" if N != 0 and (N & (N-1) ==0) else "no")
