a = int(raw_input())
s, r = [int(x) for x in raw_input().split(" ")]
print("yes" if (a > s and a < r) else "no")
