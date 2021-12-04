import datetime
from helpers import isEvenWeek
from icalendar import Event

def addFirstHalf(cal, course, classType, title, indexNumber, startDay, duration, venue, recessDate, biWeekly):
    event = Event()
    event.add('summary', "{} {} {}".format(course, classType, title))
    event.add('description', indexNumber)
    event.add('dtstart', startDay)
    event.add('duration', duration)
    event.add('dtstamp', datetime.datetime.today())
    event.add('location', venue)
    if biWeekly:
        event.add('rrule', {'freq' : 'weekly','interval' : 2, 'until' : recessDate})
    else:
        event.add('rrule', {'freq' : 'weekly', 'until' : recessDate})
    cal.add_component(event)
    return

def addSecondHalf(cal, course, classType, title, indexNumber, duration, venue, endDate, biWeekly, startTime, startDate, recessWeek, dayInt, remarks):
    if recessWeek%2 == 0:
        # week after recess week is a even week
        if isEvenWeek(remarks):
            startDay = startDate + datetime.timedelta(weeks=recessWeek+1, days=dayInt)
        else:
            startDay = startDate + datetime.timedelta(weeks=recessWeek+2, days=dayInt)
    else:
        # week after recess week is a odd week
        if isEvenWeek(remarks):
            startDay = startDate + datetime.timedelta(weeks=recessWeek+2, days=dayInt)
        else:
            startDay = startDate + datetime.timedelta(weeks=recessWeek+1, days=dayInt)
    startDay += datetime.timedelta(hours=startTime.hour, minutes=startTime.minute)
    
    event = Event()
    event.add('summary', "{} {} {}".format(course, classType, title))
    event.add('description', indexNumber)
    event.add('dtstart', startDay)
    event.add('duration', duration)
    event.add('dtstamp', datetime.datetime.today())
    event.add('location', venue)
    if biWeekly:
        event.add('rrule', {'freq' : 'weekly','interval' : 2, 'until' : endDate})
    else:
        event.add('rrule', {'freq' : 'weekly', 'until' : endDate})
    cal.add_component(event)
    return

if __name__ == '__main__':
    createCalendar()