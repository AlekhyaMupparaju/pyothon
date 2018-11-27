def isIsogram(a):
	charMap = {}
	for c in a:
		if c in charMap:
			return False
		else:
			charMap[c] = 1
	return True
a = raw_input().rstrip()
print("Yes" if isIsogram(a) else "No")
