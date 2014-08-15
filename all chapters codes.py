print ("Hello There!!!") # Week 1

name = input("What is your name? ")  # Week 2
print ("Hello", name)

hrs = input("How many hours do you work a week? ")  # Week 2
hrs_1 = float(hrs)
pay = input("And how much do you make an hour? ")
pay_1 = float(pay)
total = hrs_1 * pay_1
print ("Wow you make $",total, "a week!!!")


lst = list()
lst.append(21)
lst.append(183)
print (lst)
lst[0] = 23
print (lst)

ddd = dict()
ddd['age'] = 21
ddd['course'] = 182
print (ddd)
ddd['age'] = 23
print (ddd)

ccc = dict()
ccc['csev']= 1
ccc['cwen']= 2
print (ccc)
ccc['cwen']=ccc['cwen']+1
print (ccc)

    # When we see a new name: when we encounter a new name, we need to add a
    # new entry in the dict and if this is the second time or later time we
    # have seen the name, we simply add one to the count in the dict
    # under that name.

counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for name in names:
    counts[name]= counts.get(name,0)+1
print(counts)

counts = dict()
print ('Enter a line of text:')
line = input('')

words = line.split()
print ('Words:', words)

print ('Counting..')
for word in words:
    counts[word]=counts.get(word,0) +1

print ('Counts', counts)


jjj = {'chuck':1, 'fred':42, 'jan':100}
print (list(jjj))

print (jjj.keys())
print (jjj.values())
print (jjj.items())

