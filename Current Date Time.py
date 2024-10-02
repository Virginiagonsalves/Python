'''Program that gets the current date and prints the day of the week.'''
import datetime
current_date=datetime.datetime.now()
day_of_week=current_date.strftime("%A")
print("Today is:",day_of_week)
