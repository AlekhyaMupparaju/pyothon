r=raw_input()
"""if all(c in '01' for a in r):
    print "yes"
else:
    print "No"
    """
if not(r.translate(None,'01')):
    print "yes"
else:
    print "No"
