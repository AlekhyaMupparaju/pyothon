a = raw_input().rstrip()
digits = []
for c in a:
	if c.isdigit():
		digits.append(c)
print("".join(digits))
