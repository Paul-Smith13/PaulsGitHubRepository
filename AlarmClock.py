#Simple alarm lock
#Imports the datetime module
import datetime

#Imports the time module
import time

#Gets current hour
current_hour = datetime.datetime.now().hour
#Gets current minute
current_minute = datetime.datetime.now().minute
#Gets current second
current_second = datetime.datetime.now().second

#Uses above variables to create a string of the current time
current_time = (str(current_hour) + ":" 
                + str(current_minute) + ":"
                + str(current_second))

#Tells the user what the current time is
print(f"""The current time is: 
{current_time}
        """)

#Function where user sets an alarm
def set_alarm():
    alarmHour = int(input("What hour do you want to set the alarm to? \n>"))
    alarmMinute = int(input("What minute do you want to set the alarm to? \n>"))
    alarmSecond = int(input("What second do you want to set the alarm to? \n>"))
    
    while (1 == 1):
        if(alarmHour == datetime.datetime.now().hour and 
        alarmMinute == datetime.datetime.now().minute and 
        alarmSecond == datetime.datetime.now().second):
            print(f"It is now {datetime.datetime.now()}")
            break
 
#Function where user sets timer
def set_timer():
    print("""
    You have chosen to set a timer.
    """)
    timer_hours= int(input("How many hours would you like the timer to go off in? \n>"))
    timer_minutes= int(input("How many minutes would you like the timer to go off in? \n>"))
    timer_seconds= int(input("How many seconds would you like the timer to go off in? \n>"))
    print(f"The timer will go off in {timer_hours} hours {timer_minutes} minutes {timer_seconds} seconds.")
    
    target_time = (str(current_hour + timer_hours) + ":" + 
                    str(current_minute + timer_minutes) + ":" +
                    str(current_second + timer_seconds))
    print("The timer is scheduled to go off at ", target_time)
    
    timer = (timer_hours * 60 * 60 + timer_minutes * 60 + timer_seconds)
    
    for i in range(timer):
        print(str(timer - i) + " seconds remaining")
        time.sleep(1)
    
    print("TIME UP")

#Function takes input from user allowing them to choose whether they'd like to set an alarm or timer.    
def alarm_or_timer_choice():
    print("""
    You can either choose to set an alarm or timer.
    To set an alarm please enter 1.
    To set a timer please enter 2.
    """)
    user_choice = int(input("> "))
    if user_choice == 1:
        set_alarm()
    elif user_choice == 2:
        set_timer()
    else:
        print("You did not select either option. \n EXITING.")
        
#Calls the alarm_or_timer_choice function, beginnning the program.        
alarm_or_timer_choice()
      


    


