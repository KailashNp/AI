import time
import os

def convert(t):
    return t*60

def countdown(t,label):
    while t:
        min, sec= divmod(t,60)
        print(f"{label}: {min:02d}:{sec:02d}", end="\r")
        time.sleep(1)
        t-=1
        
def timer(work):
    w=convert(work)
    countdown(w,"Work")
    os.system("clear||cls")
    
    
work=int(input("Enter work time (min):"))

timer(work)
