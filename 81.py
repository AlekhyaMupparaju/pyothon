def do_stuff(input):
	a, b = [int(a) for a in input.split(" ")]
	print(b-a)
		

while True:
  try:
    value = raw_input()
    do_stuff(value.rstrip()) # next line was found 
  except (EOFError):
    break #end of file reached
