import threading
import time

def timer():
  print()
  print()
  count = 0
  while True:
    time.sleep(1)
    count += 1
    print("Logged in for:", count, "Seconds")

x = threading.Thread(target=timer, daemon=True)
x.start()

x.setDaemon(True)
print(x.isDaemon())

answer = input("Do you wish to exit?")
