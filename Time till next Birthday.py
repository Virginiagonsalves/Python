'''Write a program that takes a birthday as input and prints the user’s age and the number of days, hours,
minutes and seconds until their next birthday.'''
from datetime import datetime,timedelta
def get_age_and_time_until_next_birthday(birthday):
    current_date=datetime.now()
    birthday_date=datetime.strptime(birthday,"%Y-%m-%d")
    age=current_date.year-birthday_date.year
    if(current_date.month,current_date.day)<(birthday_date.month,birthday_date.day):
        age-=1
    next_birthday=birthday_date.replace(year=current_date.year)
    if next_birthday<current_date:
        next_birthday=next_birthday.replace(year=current_date.year+1)
    time_until_next_birthday=next_birthday-current_date
    days_until_next_birthday=time_until_next_birthday.days
    hours_until_next_birthday,remainder=divmod(time_until_next_birthday.seconds,3600)
    minutes_until_next_birthday,seconds_until_next_birthday=divmod(remainder,60)
    print("Your age:",age)
    print("time until your next birthday:")
    print(days_until_next_birthday,"days",hours_until_next_birthday,"hours",minutes_until_next_birthday,"minutes",seconds_until_next_birthday,"seconds")
birthday=input("Enter your birthday(YYYY-MM-DD):")
get_age_and_time_until_next_birthday(birthday)
