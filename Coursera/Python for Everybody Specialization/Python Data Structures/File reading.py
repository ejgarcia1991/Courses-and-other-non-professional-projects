# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
x=0
tot=0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    pos=line.find(":")
    l=line[pos+1:]
    l=l.strip()
    tot+=float(l)
    x+=1
print("Average spam confidence: "+str(tot/x))
