import calendar

def week_day_name(date):
    date = date.split()
    year = int(date[2])
    month = int(date[0])
    day = int(date[1])
    dayNumber = calendar.weekday(year, month, day)
    dayName = ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"]
    return dayName[dayNumber]

Date = input("Introduce date format MM DD YYYY: ")
print(week_day_name(Date)) 