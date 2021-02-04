name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

hours={}
for line in handle:
    l=line.strip()
    if line.startswith("From "):
        pos=l.find(":")
        hour=l[pos-2:pos]
        hours[hour]=hours.get(hour,0)+1

lsort=sorted([(k,v) for k,v in hours.items()])
for pair in lsort:
    print(pair[0],pair[1])