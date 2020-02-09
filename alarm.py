"""This program allows the user to set one or two alarm clocks.
It also displays the current time and sounds when the alarm fires """
"""Author: Tony Chisenga"""

import time
from playsound import playsound

class alarm:
    #constructor for the alarm class
    def __init__(self,alarm_time):
        self.alarm_time = alarm_time

    #getter method
    def get_alarm_time(self):
        return self.alarm_time

    #setter method
    def set_alarm_time(self,t):
        self.alarm_time = t

    #method to check alarm
    def fire_alarm(self):    
        while(1==1):
            #get current time
            t = time.localtime()
            current_time = time.strftime("%H:%M:%S", t)

            #get hours and minutes from alarm time and current time
            split_cur_time = current_time.split(':')
            split_alarmtime_time = self.alarm_time.split(':')
            alarmtime_hour = split_alarmtime_time[0]
            alarmtime_min = split_alarmtime_time[1]
            curtime_hour = split_cur_time[0]
            curtime_min = split_cur_time[1]

            #check if its time
            if(alarmtime_hour==curtime_hour and alarmtime_min==curtime_min):
                print("Its time!!!")
                playsound('fire.mp3')
                break 
    
                
        
        
#the main method  
if __name__ == "__main__":

    #display current time
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    print("The current time is ",current_time)

    #get how many times the user wants to set alarm
    num_of_alarms = input("Enter 1 to set 1 alarm, 2 to set 2 larms: ")

    #set one alarm
    if num_of_alarms == "1":
        alarm_time = input("Set alarm time in format HH:MM:SS: ")
        alarm_one = alarm(alarm_time)
        print("Alarm set")
        alarm_one.fire_alarm()

    #set two alarms
    elif num_of_alarms == "2":
        first_alarm_time = input("Set 1st alarm time in format HH:MM:SS: ")
        alarm_one = alarm(first_alarm_time)
        print("first alarm set")
        second_alarm_time = input("Set 2nd alarm time in format HH:MM:SS: ")
        print("second alarm set")
        alarm_one.fire_alarm()
        alarm_one.set_alarm_time(second_alarm_time)   
        alarm_one.fire_alarm()

    #invalid choice from the ser
    else:
        print("Invalid input")

        
        

    
