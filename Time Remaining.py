'''Write a function called print_time that takes two Time objects and prints total time remained in the form
hour:minute:second.'''
class Time:
    def __init__(self,hour,minute,second):
     self.hour=hour
     self.minute=minute
     self.second=second
def print_time(time1,time2):
    total_seconds=(time1.hour+time2.hour)*3600+(time1.minute+time2.minute)*60+(time1.second+time2.second)
    total_hours=total_seconds//3600
    remaining_seconds=total_seconds%3600
    total_minutes=remaining_seconds//60
    total_seconds=remaining_seconds%60
    print("Total time:",total_hours,"hours:",total_minutes,"minutes:",total_seconds,"seconds")
time1=Time(2,30,45)
time2=Time(1,15,20)
print_time(time1,time2)
