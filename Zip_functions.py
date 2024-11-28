usernames = ["A" , "B" , "C"]
passwords = ["AA", "BB", "CC"]

# users = list(zip(usernames, passwords))
# users = dict(zip(usernames, passwords))

# for key, value in users.items():
#   print(key + " : " + value)

login_date =["1/1/2021", "1/2/2021", "1/3/2021"]

users = zip(usernames, passwords, login_date)

for i in users:
  print(i)