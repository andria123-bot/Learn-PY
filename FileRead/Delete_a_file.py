import os

path = './fileRead/Test.txt'

try:
  os.remove(path) # delete a file
  # os.rmdir(path) # delete an empty directory
  # shutil.rmtree(path) # delete a directory containing files
except FileNotFoundError:
  print('that file does not exist')
except PermissionError:
  print('you do not have permission to delete that file')
except OSError:
  print('You cannot delete that file using that function')
else:
  print(path + "was deleted")