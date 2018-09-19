r=raw_input()
vo=set('aeiou')
if not vo.isdisjoint(r):
    print "yes"
else:
    print "no"
