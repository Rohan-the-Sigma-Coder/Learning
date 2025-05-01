import re
import math
time = input('Enter time (with colon): ' )
time_list = time.split(':')
if int(time_list[0]) > 12 or int(time_list[1]) > 59:
    print('Invalid response')
    quit()
time_list[0] = int(time_list[0])
time_list[1] = int(time_list[1])
hour_hand_degrees = ((time_list[0] + time_list[1]/60) * 30)
minute_hand_degrees = int(time_list[1]) * 6
print(f'The degree difference between the hour hand and the minute hand is {abs(minute_hand_degrees - hour_hand_degrees)} degrees and {abs(360 - (hour_hand_degrees - minute_hand_degrees))} degrees')