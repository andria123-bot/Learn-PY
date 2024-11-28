# squares = []
# for i in range(1, 11):
#   squares.append(i * i)
# print(squares)

# squares = [i * i for i in range(1, 11)]; print(squares) # 1 line code

students = [100, 90, 80, 70, 60, 50, 40 ,30, 0]

# passed_students = [i for i in students if i >= 60]
passed_students = [i if i >= 60 else "FAILED" for i in students]
# passed_students = list(filter(lambda x: x >= 60, students))
print(passed_students)