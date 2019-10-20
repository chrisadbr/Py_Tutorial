# Program to elaborate Einstein Puzzle'


def reverse_num(num):
    rev_num = 0
    while num > 0:
        rev_num = (rev_num * 10) + (num % 10)
        num //= 10
    return rev_num


def get_rev_diff(num1, num2):
    return abs(num1 - num2)


def get_rev_sum(a, b):
    return a + b


number = int(input('Enter a number: '))
answer = reverse_num(number)
print("\nFor the number: " + str(number) + " reverse number is: " + str(answer))
revDiff = get_rev_diff(number, answer)
print("The difference between " + str(answer) + " and " + str(number) + " is " + str(revDiff))
answer2 = reverse_num(revDiff)
print("The reverse difference is: " + str(answer2))
answer3 = get_rev_sum(answer2, revDiff)
print("The sum of: " + str(revDiff) + " and " + str(answer2) + " is " + str(answer3))
