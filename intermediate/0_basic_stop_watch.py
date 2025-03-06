import time
import os 
from datetime import datetime

def cls():
    os.system("cls" if os.name=="nt" else "clear")

cls()

print("BASIC STOPWATCH 1.0\n-------------------")
print("\nPress Enter to Start and Stop")


input()
start_time = time.time()
print("\tStart Time :", time.strftime("%H : %M : %S", time.localtime()), end=" ")

input()
end_time = time.time()
print("\tEnd Time   :", time.strftime("%H : %M : %S", time.localtime()))

print(f"\tTime Elapsed in Seconds : {end_time-start_time : .2f} ")