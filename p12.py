_,NN = map(int,raw_input().split(" "))
data = map(int,raw_input().split(" "))
L = len(data)
for __ in range(NN):
    data = [data[L-1]] + data[0:L-1]
print " ".join(map(str,data))
