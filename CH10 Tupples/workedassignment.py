fhand = open('romeo.txt')
counts = dict()
for line in fhand:
    words = line.split()
    for word in words:
        wrd = word.lower()
        counts[wrd] = counts.get(wrd, 0) + 1


flipped = list()
for kie, vaal in counts.items() :
    newtup = (vaal, kie)
    print (newtup)
    flipped.sort(reverse=True)
    
print (flipped[:5])

for kay, vall in flipped[:5]:
    print (kay, vall)
