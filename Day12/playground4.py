import time

test_array = []
test_line = []
for a in range(100):
    for b in range(100):
        test_line.append([a,a+b])
    test_array.append(test_line)

time_start = time.time()
newlist1 = []
for sublist in test_array:
    newlist1.append(list(reversed(sublist)))
time_stop = time.time()
# print(f'Attempt 1 result: {newlist1}')
print(f'Time passed: {time_stop-time_start}')
print('-----------------------\n')

time_start = time.time()
newlist2 = list(map(lambda x: list(reversed(x)), test_array))
time_stop = time.time()
# print(f'Attempt 2 result: {newlist2}')
print(f'Time passed: {time_stop-time_start}')
print('-----------------------\n')

time_start = time.time()
newlist3 = [i[::-1] for i in test_array]
time_stop = time.time()
# print(f'Attempt 3 result: {newlist3}')
print(f'Time passed: {time_stop-time_start}')
print('-----------------------\n')

time_start = time.time()
newlist4 = list(map(lambda x: x[::-1], test_array))
time_stop = time.time()
# print(f'Attempt 4 result: {newlist4}')
print(f'Time passed: {time_stop-time_start}')
print('-----------------------\n')