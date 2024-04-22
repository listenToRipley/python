# import datetime
from datetime import datetime, timedelta
# future_date = datetime.date(2222, 9,20)
# print(f"Future date: {future_date}")

# print(future_date.year)
# print(future_date.month)
# print(future_date.day)

# some_time = datetime.time(15,30,10)

# print(f"Some time: {some_time}")

# print(some_time.hour)
# print(some_time.minute)
# print(some_time.second)

new_future_datetime = datetime(2100, 10,12,20,55,15)
print(f"Future date and time {new_future_datetime}")

print(dir(new_future_datetime))

# change format
print(f"Format date: {new_future_datetime.strftime("%B %d, %Y")}")
print(f"Format time: {new_future_datetime.strftime("%I:%M %p")}")
print(f"Format date and time: {new_future_datetime.strftime("%A, %B %d, %Y %I:%M %p")}")

# from string to formatted time 

format_datetime_str = "3000-11-20 14:25:45"

parsed_datetime = datetime.strptime(format_datetime_str, "%Y-%m-%d %H:%M:%S")
print(parsed_datetime)
print(parsed_datetime.year)

parsed_date = datetime.strptime("June 30, 2050", "%B %d, %Y")
print(parsed_date)

parsed_time = datetime.strptime("10:12 AM", "%I:%M %p")
print(parsed_time)

#add data to object
# add time
print(new_future_datetime + timedelta(days=100, hours=3, minutes=50))
# subtract time 

print(new_future_datetime - timedelta(days=365, hours=23, minutes=50))