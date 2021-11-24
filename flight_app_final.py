import random
import time

prompt = input ("Take a flight? or Automate flights?")


def Probability():
        auto_flights= random.randint(1,10000000)
        print(auto_flights)
        
        if auto_flights == 5000000:
                print("Crash")
        else:
                print("Safe Flight")
                

if prompt == "Take a flight":
        print("Flying")
        time.sleep(1)
        Probability()
while prompt == "Automate flights":
        Probability()

