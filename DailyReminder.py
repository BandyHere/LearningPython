from time import time, ctime
import random
import time 


print("What do you want me to remind you about?")
text = str(input())
print("In how many minutes would you like me to remind you?")
local_time = float(input())
local_time = local_time * 60
time.sleep(local_time)
print(text)

