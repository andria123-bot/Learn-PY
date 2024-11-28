import os

source = 'file'
destination = 'C:\\Users\\andria.DESKTOP-1EU1TK7\\Desktop\\Test2.txt'

try:
  if os.path.exists(source):
    print('There is areadly a file theere')
  else:
    os.replace(source, destination)
    print(source + 'mooved')

except FileNotFoundError:
  print(source + ' was not found')