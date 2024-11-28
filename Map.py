store = [
  ("Shirt", 20.00),
  ("Pants", 25.00),
  ("Jacket", 50.00),
  ("Socks", 10.00)]

to_euros = lambda data: (data[0], data[1] * 0.82) # Euros
to_dollars = lambda data: (data[0], data[1] / 0.82) # Dollar

store_dollars = list(map(to_dollars, store))
store_euros = list(map(to_euros, store))

for i in store_dollars:
  print(i)