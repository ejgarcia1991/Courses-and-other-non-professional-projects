# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
for line in fh:
    l=line.rstrip()
    print(l.upper())