try:
  with open('./fileRead/text.txt') as file:
    print(file.read())
except FileNotFoundError:
  print('File not found.')
# print(e.message)le.closed()) # close the file