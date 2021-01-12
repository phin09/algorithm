# https://www.acmicpc.net/problem/1924

# 방법 1
# https://docs.python.org/3/library/datetime.html#datetime.date.weekday
import sys
from datetime import date

x, y = map(int, sys.stdin.readline().split(' '))
dayArr = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
date = dayArr[date(2007, x, y).weekday()]
print(date)

# 방법 2
import sys

x, y = map(int, sys.stdin.readline().split(' '))
month = {1: 0, 2:31, 3:31+28, 4:31+28+31, 5:31+28+31+30, 6:31+28+31+30+31,
         7:31+28+31+30+31+30, 8:31+28+31+30+31+30+31,
         9:31+28+31+30+31+30+31+31, 10:31+28+31+30+31+30+31+31+30,
         11:31+28+31+30+31+30+31+31+30+31, 12:31+28+31+30+31+30+31+31+30+31+30}
temp = month[x] + y
day = {0:'SUN', 1:'MON', 2:'TUE', 3:'WED', 4:'THU', 5:'FRI', 6:'SAT'}
print(day[temp%7])