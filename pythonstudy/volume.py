'''
f = open('cont.txt')
line = f.readline()
f.close()

words = line.split(' ')

bins = {}
for word in words:
    if not word in bins:
        bins[word] = 0
    bins[word] += 1

rst = list(bins.items())
rst = [(i[1],i) for i in rst]
rst.sort(reverse=True)
print([i[1] for i in rst])
'''

a = 5
b = 4
