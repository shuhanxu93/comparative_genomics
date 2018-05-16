import sys, re

bHandle = open (sys.argv [1])



list_09 = []
list_17 = []
list_49 = []
list_51 = []



lines = bHandle.readlines ()

id = 0

for aLine in lines:

	aLine = aLine.replace ("\n", "")
	words = aLine.split ()

	for aWord in words:

		if aWord.startswith('./09'):
		    list_09.append(aWord)
		elif aWord.startswith('./17'):
		    list_17.append(aWord)
		elif aWord.startswith('./49'):
		    list_49.append(aWord)
		else:
		    list_51.append(aWord)

print(len(list_09), len(list_17), len(list_49), len(list_51))
print(len(set(list_09)), len(set(list_17)), len(set(list_49)), len(set(list_51)))
