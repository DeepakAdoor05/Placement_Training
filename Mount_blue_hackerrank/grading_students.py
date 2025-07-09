def gradingStudents(grades):
    # Write your code here
    list = []
    for i in grades:
        if i < 38:
            list.append(i)
        else:
            next_value = (i//5+1)*5
            diff_value = next_value - i
            if diff_value < 3:
                list.append(next_value)
            else:
                list.append(i)
    return list

grades_count = int(input().strip())
grades = []
for _ in range(grades_count):
    grades_item = int(input().strip())
    grades.append(grades_item)
print(gradingStudents(grades))

# Sample Input 0
# 4
# 73
# 67
# 38
# 33

# Sample Output 0
# 75
# 67
# 40
# 33