student = ("Andria", 21, "male")

print(student.count("Andria"))
print(student.index("male"))

for x in student:
  print(x)

if "Andria" in student:
  print("Andria is in the list.")