name = input('Enter file:')
handle = open(name)
if len(name)<1 : name = "mbox-short.txt"
counts = dict()
for line in handle:
    words=line.split()
    if len(words) < 2 : continue
    if words[0] != "From" : continue
    email = words[1]
    counts[email] = counts.get(email, 0) + 1

bigcount = None
bigname = None
for name, count in counts.items():
    if bigname is None or count > bigcount:
        bigname = name
        bigcount = count
print (bigname, bigcount)
