fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
	l=line.rstrip()
	spl=l.split()
	for word in spl:
		if not word in lst:
			lst.append(word)
lst.sort()
print(lst)