from datetime import datetime
from datetime import date
from datetime import time
from datetime import timedelta

# construct a basic timedelta and print it
print timedelta(days=365, hours=5, minutes=1)

# print today`s date
print "today is: " + str(datetime.now())

#print today`s date one year from now
print "one year from now it will be: " + str(datetime.now() + timedelta(days=365))

# timedelta that uses more than one argument
print "in two weeks and 3 days it will be: " + str(datetime.now() + timedelta(weeks=2, days=3))

# the date 1 week ago, formatted as a string
t = datetime.now() - timedelta(weeks=1)
s = t.strftime("%A %B %d, %Y")
print "one week ago it was " + s

# how many days until April Fool`s Day?
today = date.today() # get today`s date
afd = date(today.year, 4, 1) # get April Fool`s has already gone for this year
if afd < today:
    print "April Fool`s day alredy went by %d days ago" %((today-afd).days)
    afd = afd.replace(year=today.year + 1) # if so, get the date for next year
# Calculate the amount of time until April Fool`s Day
time_to_afd = abs(afd - today).days
print time_to_afd, "days until next April Fool`s Day!"