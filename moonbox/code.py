data = open('file.txt').read().splitlines()

counts = []
for i in range(0,len(data)):
    count = 0
    for line in data:
        if data[i] == line:
            count += 1
    counts.append(count)

#print(counts)
majoritysentence = data[counts.index(max(counts))]
print(majoritysentence)
majoritynum = max(counts)
print(majoritynum)
