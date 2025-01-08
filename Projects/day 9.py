# average calculator
nvmlist = list()
while True:
  inp = input("Enter a number: ")
  if inp == "done": break
  value = float(inp)
  nvmlist.append(value)

average = sum(nvmlist) / len(nvmlist)
print("Average:", average)