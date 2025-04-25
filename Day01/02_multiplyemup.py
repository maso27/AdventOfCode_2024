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

mults = []
for num in list1:
    multiplier = list2.count(num)
    mults.append(multiplier * num)

print(f'Multiplier Numbers: {mults}')

print(f'Final Sum: {sum(mults)}')