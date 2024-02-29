import time
import datetime
from grovepi import *
import math

buzzer_pin = 2      #Port for buzzer
button = 7     #Port for Button
led = 4



pinMode(led,"OUTPUT")
pinMode(buzzer_pin,"OUTPUT")    # Assign mode for buzzer as output
pinMode(button,"INPUT")     # Assign mode for Button as input

def current_milli_time():
    return round(time.time() * 1000)

file_to_delete = open("output.txt", 'w')
file_to_delete.close()

while True:
    try:
        ms = current_milli_time()
        button_status= digitalRead(button)  #Read the Button status
        if button_status:   #If the Button is in HIGH position, run the program
            digitalWrite(buzzer_pin,1)
            with open('output.txt', 'a') as f:
                print('1 ', ms, ' ', datetime.datetime.fromtimestamp(ms/1000) , file = f)
            digitalWrite(led,1) 
        else:       #If Button is in Off position, print "Off" on the screen
            digitalWrite(buzzer_pin,0)
            with open('output.txt', 'a') as f:
                print('0 ', ms, ' ', datetime.datetime.fromtimestamp(ms/1000), file = f)
            digitalWrite(led,0) 
    except KeyboardInterrupt:   # Stop the buzzer before stopping
        digitalWrite(buzzer_pin,0)
        break
    except (IOError,TypeError) as e:
        print("Error")