import math
time = input('Enter time (with colon): ' )
time_list = time.split(':')
try:
    hour = int(time_list[0])
    minute = int(time_list[1])
except :
     print('Invalid Response')
     quit()
def varification(hour, minute):
    if hour > 12 or hour < 1 or minute > 59 or minute    < 0:
        print('Invalid Response')
        quit()
def time_to_degrees(hour, minute):
    varification(hour, minute)
    hour_hand_degrees = (hour + minute/60) * 30
    minute_hand_degrees = int(minute) * 6
    return minute_hand_degrees - hour_hand_degrees


print(time_to_degrees(hour, minute))



