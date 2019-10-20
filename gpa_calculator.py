# Program to calculate GPA

valid_grade = ['a', 'b+', 'b', 'c', 'd', 'e', 'f']
total_hrs = 0
total_points = 0
total_credits = 0
while True:
    get_grade = input("Please enter a grade: ").lower()
    if get_grade == 'quit':
        break
    else:
        if get_grade not in valid_grade:
            print('Not a valid grade')
            continue
        else:
            hrs = int(input("Enter number of Hours: "))
        if get_grade == 'a':
            total_hrs += hrs
            total_points += (hrs * 5)
        elif get_grade == 'b+':
            total_hrs += hrs
            total_points += (hrs * 4)
        elif get_grade == 'b':
            total_hrs += hrs
            total_points += (hrs * 3)
        elif get_grade == 'c':
            total_hrs += hrs
            total_points += (hrs * 2)
        elif get_grade == 'd':
            total_hrs += hrs
            total_points += (hrs * 1)
        elif get_grade == 'e':
            total_hrs += hrs
            total_points += (hrs * 0.5)
        elif get_grade == 'f':
            total_hrs += hrs
            total_points += (hrs * 0)

gpa = float(total_points / total_hrs)
gpa = round(gpa, 2)
print("Wighted GPA: ", gpa)