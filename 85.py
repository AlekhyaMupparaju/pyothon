a = raw_input().rstrip()
evenS = odda = ''
for i, c in enumerate(a):
	if i & 1 == 0:
		evena += c
	else:
		odda += c

print(evena + " " + odda)
