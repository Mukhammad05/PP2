# task 1
import datetime

today = datetime.datetime.now()
One_friday_ago = today - datetime.timedelta(days=5)

print(today.strftime("%d - %m - %y"))
print(One_friday_ago.strftime("%d - %m - %y"))

# task 2
import datetime


today = datetime.datetime.now()
yesterday = today - datetime.timedelta(days=1)
tomorrow = today + datetime.timedelta(days=1)

print("Yesterday: ",yesterday.strftime("%d-%m-%y"))
print("Today: ",today.strftime("%d-%m-%y"))
print("Tomorrow: ",tomorrow.strftime("%d-%m-%y"))

# task 3
import datetime

time_today = datetime.datetime.now()

print(time_today.strftime("%H:%M:%S"))

# task 4
from datetime import datetime

def date_difference_in_seconds(date1, date2):
    dt1 = datetime.strptime(date1, '%H:%M:%S')
    dt2 = datetime.strptime(date2, '%H:%M:%S')

    time_difference = dt2 - dt1

    difference_in_seconds = time_difference.total_seconds()

    return difference_in_seconds

if __name__ == "__main__":
    date1 = input("Enter the first date (HH:MM:SS): ")
    date2 = input("Enter the second date (HH:MM:SS): ")

    difference = date_difference_in_seconds(date1, date2)
    print("Difference in seconds:", difference)


