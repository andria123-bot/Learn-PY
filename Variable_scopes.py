name = "Andria" # Global variable & scope (avable everywhere in the script)

def display_name():
  name = "Lezhava" # Local variable & scope (avable only inside this function)
  print(name)

display_name()
print(name)