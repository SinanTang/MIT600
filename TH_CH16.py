### Think Python 2 Ch.16 Classes and Functions

import datetime
# from datetime import date
from datetime import datetime, date
# import time

class Time:
    """
    represents the time of day.
    attributes: hour, minute, second
    """


time = Time()
time.hour = 11
time.minute = 5
time.second = 30

time2 = Time()
time2.hour = 1
time2.minute = 5
time2.second = 37


def print_time(t):
    second = int(round(t.second))
    minute = int(round(t.minute))
    hour = int(round(t.hour))
    print("{:02d}:{:02d}:{:02d}".format(hour, minute, second))


# print_time(time)

def is_after(t1, t2):
    return t1.hour > t2.hour or (t1.hour == t2.hour and t1.minute > t2.minute) \
           or (t1.hour == t2.hour and t1.minute == t2.minute and t1.second > t2.second)


# print(is_after(time2, time))


# prototype and patch
def add_time(t1, t2):
    sum = Time()
    sum.hour = t1.hour + t2.hour
    sum.minute = t1.minute + t2.minute
    sum.second = t1.second + t2.second
    return sum

start = Time()
start.hour = 9
start.minute = 45
start.second = 0

duration = Time()
duration.hour = 1
duration.minute = 30
duration.second = 0

# done = add_time(start, duration)
# print_time(done)

# functional programming
def add_time2(t1, t2):
    sum = Time()
    # sum.second = (t1.second + t2.second) % 60
    minutes, sum.second = divmod(t1.second + t2.second, 60)
    # sum.minute = (t1.minute + t2.minute + (t1.second + t2.second)//60) % 60
    hours, sum.minute = divmod(t1.minute + t2.minute + minutes, 60)
    # sum.hour = (t1.hour + t2.hour + (t1.minute + t2.minute + (t1.second + t2.second)//60)//60)% 60
    sum.hour = divmod(t1.hour + t2.hour + hours, 24)[1]
    return sum

# done2 = add_time2(start, duration)
# print_time(done2)


# designed development: time as base 60 numbers
def time_to_int(time):
    minutes = time.hour * 60 + time.minute
    seconds = minutes * 60 + time.second
    return seconds

def int_to_time(seconds):
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time

def add_time3(t1, t2):
    seconds = time_to_int(t1) + time_to_int(t2)
    return int_to_time(seconds)

# done3 = add_time3(start, duration)
# print_time(done3)

def increment(time, seconds):
    seconds = time_to_int(time) + seconds
    return int_to_time(seconds)

# print_time(increment(start, 3600))


# Defining invariants to help debugging
def valid_time(time):
    if time.hour < 0 or time.minute < 0 or time.second < 0:
        return False
    if time.minute >= 60 or time.second >= 60:
        return False
    return True

def add_time4(t1, t2):
    if not valid_time(t1) or not valid_time(t2):
        raise ValueError('invalid Time object in add_time4')
    # or assert statement
    # assert valid_time(t1) and valid_time(t2)
    seconds = time_to_int(t1) + time_to_int(t2)
    return int_to_time(seconds)



## Exercise 16.1
def mul_time(t, num):
    assert valid_time(t)
    seconds = time_to_int(t)
    return int_to_time(seconds*num)

# print_time(mul_time(duration, 2))

def average_pace(t, distance):
    assert valid_time(t)
    assert distance > 0
    return mul_time(t, 1/distance)

# print_time(average_pace(duration, 8))


## Exercise 16.2

# 1
weekdays = {0:'Monday', 1:'Tuesday', 2:'Wednesday', 3:'Thursday', 4:'Friday', 5:'Saturday', 6:'Sunday'}

def print_date_weekday():
    t = datetime.date.today()
    wd = weekdays[t.weekday()]
    print("Today is {} {}-{}-{}.".format(wd,t.day,t.month,t.year))

# print_date_weekday()

# 2
def birthday(y, m, d):
    # today = datetime.date.today() # y,m,d
    today = datetime.now().replace(microsecond = 0)

    if today.month > m or (today.month == m and today.day > d):
        next_bday = datetime(today.year+1, m, d, 0,0,0)
        age = today.year - y
    else:
        next_bday = datetime(today.year, m, d, 0,0,0)
        age = today.year - y - 1
    # print(next_bday)
    time_to_bday = next_bday - today
    days = time_to_bday.days
    hours = time_to_bday.seconds // 3600
    minutes = (time_to_bday.seconds)%3600 // 60
    seconds = time_to_bday.seconds % 60

    print('You are {} years old!'.format(age))
    print('You have {} days {} hours {} minutes and {} seconds until your next Birthday!'.format(days,hours,minutes,seconds))

# birthday(1992,7,16)
# birthday(1992,9,26)


# 3
def is_older(y1,m1,d1, y2,m2,d2):
    """
    returns true if the first date is earlier/older than the second
    """
    return (y1<y2) or (y1==y2 and m1<m2) or (y1==y2 and m1==m2 and d1<d2)

# print(is_older(1992,8,7, 1992,7,6))

def difference_in_days(y1,m1,d1, y2,m2,d2):
    """
    returns the difference between 2 dates in days
    """
    date1 = date(y1,m1,d1)
    date2 = date(y2,m2,d2)
    return abs(date2 - date1)


def double_day(y1,m1,d1, y2,m2,d2):
    # d_day = date(y,m,d)
    # while y >= max(y1,y2):
    #     for m in range(1,13):
    #         for d in range(1,32):
    #             if difference_in_days(y,m,d, y1,m1,d1) == difference_in_days(y,m,d, y2,m2,d2) * 2:
    #                 return date(y,m,d)
    bdays1 = date(y1,m1,d1).toordinal()
    bdays2 = date(y2,m2,d2).toordinal()
    i = max(bdays1, bdays2)
    while True:
        if (i - bdays1) == (i - bdays2)*2 or (i - bdays2) == (i - bdays1)*2:
            return date.fromordinal(i)
        i += 1

# print(double_day(2000,1,1, 2003,2,1))


def n_times_day(y1,m1,d1, y2,m2,d2, n):
    assert n >= 1
    bdays1 = date(y1, m1, d1).toordinal()
    bdays2 = date(y2, m2, d2).toordinal()
    i = max(bdays1, bdays2)
    while True:
        if (i - bdays1) == (i - bdays2) * n or (i - bdays2) == (i - bdays1) * n:
            return date.fromordinal(i)
        i += 1

# can be very slow... may exist a better solution ->
print(n_times_day(2000,1,1, 2000,2,1, 3))