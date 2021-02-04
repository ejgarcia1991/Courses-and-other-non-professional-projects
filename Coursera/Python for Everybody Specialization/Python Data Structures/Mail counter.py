name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

senders={}

for line in handle:
    l=line.strip()
    if l.startswith("From "):
        sender=l.split()[1]
        senders[sender]=senders.get(sender,0)+1

maxi=None
name=None
for key,value in senders.items():
    if(maxi==None or value>maxi):
        maxi=value
        name=key

print(name, str(maxi))