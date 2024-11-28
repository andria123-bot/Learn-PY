import os

path = 'C:\\Users\\andria.DESKTOP-1EU1TK7\\Desktop\\folder'

if os.path.exists(path):
  print("That location exists!")
  if os.path.isfile(path):
    print("That is a file")
  elif os.path.isdir(path):
    print("That is a directory!")
else:
  print("That location does not exist!")