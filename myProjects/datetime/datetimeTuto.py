import time, datetime

# time and datetime module tutorial

# time

'''
print(time.time())
now = time.time()
print(round(now, 2))
print(round(now, 4))
print(round(now))


import time
def calcProd():
       # Calculate the product of the first 100,000 numbers.
       product = 1
       for i in range(1, 1000): #   add000):
           product = product * i
       return product

startTime = time.time()
prod = calcProd()
endTime = time.time()
print('The result is %s digits long.' % (len(str(prod))))
print('Took %s seconds to calculate.' % (endTime - startTime))



for i in range(3):
    print('Tick')
    time.sleep(1)  # Waits for 1 sec
    print('Tock')
    time.sleep(1)'''


# datetime

'''print(datetime.datetime.now())
dt = datetime.datetime(2015, 10, 21, 16, 29, 0)
print(dt.year, dt.month, dt.day)
print(dt.hour, dt.minute, dt.second)
halloween2015 = datetime.datetime(2015, 10, 31, 0, 0, 0)
newyears2016 = datetime.datetime(2016, 1, 1, 0, 0, 0)
oct31_2015 = datetime.datetime(2015, 10, 31, 0, 0, 0)
print(halloween2015 == oct31_2015)   # works with all comparators
#print(halloween2015)
#print(oct31_2015)

# delta  ====  duration or range of days( not months or years)

delta = datetime.timedelta(days=11, hours=10, minutes=9, seconds=8)
print(delta.days, delta.seconds, delta.microseconds)
print(delta.total_seconds())
print(str(delta))

dt = datetime.datetime.now()   # add thousand days from now and find the moment
thousandDays = datetime.timedelta(days=365*10)  # add any no. of days
print(dt + thousandDays)  # arthematics
oct21st = datetime.datetime(2015, 10, 21, 16, 29, 0)
aboutThirtyYears = datetime.timedelta(days=365 * 30)   # this is not exact 30 years, its just the no of days 365*30 != exact 30 years
print(oct21st - (2 * aboutThirtyYears))
print(oct21st - datetime.timedelta(days=365 * 30 * 2))'''


'''  strftime()  function to display nicely
trftime directive
Meaning
%Y
Year with century, as in '2014'
%y
Year without century, '00' to '99' (1970 to 2069)
%m
Month as a decimal number, '01' to '12'
%B
Full month name, as in 'November'
%b
Abbreviated month name, as in 'Nov'
%d
Day of the month, '01' to '31'
%j
Day of the year, '001' to '366'
%w
Day of the week, '0' (Sunday) to '6' (Saturday)
%A
Full weekday name, as in 'Monday'
%a
Abbreviated weekday name, as in 'Mon'
%H
Hour (24-hour clock), '00' to '23'
%I
Hour (12-hour clock), '01' to '12'
%M
Minute, '00' to '59'
%S
Second, '00' to '59'
%p
'AM' or 'PM'
%%
Literal '%' character'''

oct21st = datetime.datetime(2015, 10, 21, 16, 29, 0)
print(oct21st.strftime('%Y/%m/%d %H:%M:%S'))
print(oct21st.strftime('%I:%M %p'))
print(oct21st.strftime("%B of '%y"))   #strftime does not need datetime.datetime

print(datetime.datetime.strptime('October 21, 2015', '%B %d, %Y'))   # reverse of strftime, it prints the datetime object
print(datetime.datetime.strptime('2015/10/21 16:29:00', '%Y/%m/%d %H:%M:%S'))
