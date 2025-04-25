filename = './Day01/input.txt'
f = open(filename, 'r')
lines = f.readlines() # reading all lines
# line = f.readline()  # reading one line
f.close()

list1 = []
list2= []

for line in lines:
    num_ascii = line.split()
    list1.append(int(num_ascii[0]))
    list2.append(int(num_ascii[1]))

# print(f'List 1: {list1}')
# print(f'List 2: {list2}')
list1.sort()
list2.sort()

# print(f'Sorted List 1: {list1}')
# print(f'sorted List 2: {list2}')

diffs = []
for a in range(len(list1)):
    diff = abs(list1[a] - list2[a])
    diffs.append(diff)

print(f'Differences: {diffs}')

print(f'Final Sum: {sum(diffs)}')