filename = './Day02/input.txt'
f = open(filename, 'r')
lines = f.readlines() # reading all lines
# line = f.readline()  # reading one line
f.close()

are_safe = []

for line in lines:

    report = list(map(int, line.split())) # convert to integers

    is_safe = True
    # establish direction
    if report[1] > report[0]:
        increasing=True
    elif report[1] < report[0]:
        increasing=False
    else:
        is_safe = False

    this_level = report.pop(0)
    for next_level in report:
        # print(f'This level: {this_level}\tNext level: {next_level}')
        diff = next_level - this_level
        this_level = next_level # get ready for the next round
        if not increasing:
            diff *= -1
        # print(f'Difference: {diff}')
        if diff < 1 or diff > 3:
            is_safe = False
            # print('NOT Safe')
    are_safe.append(is_safe)
# print(f'Safe levels: {are_safe}')
print(f'Total: {sum(are_safe)}')