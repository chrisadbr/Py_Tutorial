total = ''
count = 1
my_nums = []
for row in range(1, 10):
    for column in range(1, row + 1):
        total = str(column)
    my_nums.append(total)
    x = int("".join(my_nums))
    column_total = x * 8 + column
    print(str(x) + " * 8 " + " + " + str(column) + " = " + str(column_total))
