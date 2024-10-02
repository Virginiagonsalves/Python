'''Consider the sentence “From rjlowe@iupui.edu Fri Jan 4 14:50:18 2008”, Write python code to
extract email address and time of the day from the given sentence'''
import re
#Given sentence
sentence="From rjlowe@iupui.edu Fri Jan 4 14:50:18 2008"
#Regular expressions to extract email addresses and time of the day
email_pattern=r'From\s+([A-Za-z0-9._%+-]+@[A-Za-z0-9]+\.[A-Z|a-z]{2,})'
time_pattern=r'\b(\d{1,2}:\d{2}:\d{2})\b'
#Extract email address
email_match=re.search(email_pattern,sentence)
if email_match:
    email_address=email_match.group(1)
    print("Email address:",email_address)
#Extract time of the day
time_match=re.search(time_pattern,sentence)
if time_match:
    time_of_day=time_match.group(1)
    print("Time of the day:",time_of_day)
