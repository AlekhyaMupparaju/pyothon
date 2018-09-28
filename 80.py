s=int(raw_input())
digits = []
while s > 0:
    r = s % 10
    if r & 1 != 0:
        digits.append(str(r))
    s=s/10
digits = reversed(digits)
print (" ".join(digits))
