import time

# print(time.ctime(0)) # converts a time expressed in seconds since epoch to a readable string
#                        epoch when ur computer think time began (referance point)

# print(time.time()) # return current seconds since epoch

# print(time.ctime(time.time()))

# time_obj = time.localtime()
# time_obj = time.gmtime()
# print(time_obj)
# local_time = time.strftime("%B %d %y %H: %M %S", time_obj)

# print(local_time)

# time_string = "20 April, 2020"
# time_obj = time.strptime(time_string, "%d %b, %Y")
# print(time_obj)

time_tuple = (2020, 4, 21, 4, 22, 13, 0, 0, 0)
time_string = time.asctime(time_tuple) 
print(time_string)