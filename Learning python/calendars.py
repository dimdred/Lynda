import calendar

# create a plain text calendar
c = calendar.TextCalendar(calendar.MONDAY)
str = c.formatmonth(2013, 1, 0, 0)
print str

# create an HTML formatted calendar
hc = calendar.HTMLCalendar(calendar.MONDAY)
str = hc.formatmonth(2013, 1)
print str

# loop over the days of a month
# zeroes mean that the dat of the week is in an overlapping month
for i in c.itermonthdays(2013, 8):
    print i

# the calendar module provides useful utilities for the given locale
for name in calendar.month_name:
    print name

for day in calendar.day_name:
    print day

# The first Friday of ever month
for m in range(1,13):
    # returns an array of weeks that represent the month
    cal = calendar.monthcalendar(2013, m)
    # The first Friday has to be within the first two weeks
    weekone = cal[0]
    weektwo = cal[1]

    if weekone[calendar.FRIDAY] != 0:
        meetday = weekone[calendar.FRIDAY]
    else:
        # if the first friday isn`t in the first week, it must be in the second
        meetday = weektwo[calendar.FRIDAY]

    print "%10s %2d" %(calendar.month_name[m], meetday)