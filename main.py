import datetime
import pandas as pd
from icalendar import Calendar
from helpers import getModuleStartWeek,getStartTime,getDuration,isBiWeekly,getDay,getModuleEndWeek
from userInputs import getUserInputs
from eventAdder import addFirstHalf,addSecondHalf
from getDataFrame import getDataFrame

def createCalendar():
    cal = Calendar()

    startDate = datetime.datetime.strptime('09082021', "%d%m%Y")
    totalWeeks = 13
    recessWeek = 7
    recessDate = startDate + datetime.timedelta(weeks=recessWeek)
    
    startDate, totalWeeks, recessWeek, recessDate = getUserInputs()

    filename = input('Please input name of html file without ".html": ')
    df=getDataFrame(filename)

    #---- Iterate through the rows ----
    for i in range(len(df.index)):

        #---- If row is not Nan, move to next module
        if not pd.isnull(df.iloc[i]['Course']) or i==0:
            #---- Obtain class type
            title = df.iloc[i]['Title']
            course = df.iloc[i]['Course']

        #---- If row is Nan, still on the same module ----
        #---- Obtain group
        group = df.iloc[i]['Group']
        indexNumber = df.iloc[i]['IndexNumber']
        classType = df.iloc[i]['ClassType']
        
        # default end date
        endDate = startDate + datetime.timedelta(weeks=totalWeeks+1)
        
        # get number of weeks for module
        endWeeks = getModuleEndWeek(df.iloc[i]['Remark'])
        if endWeeks > recessWeek:
            afterRecessWeek = True
            endDate = startDate + datetime.timedelta(weeks=endWeeks+1)
        else:
            afterRecessWeek = False
            endDate = startDate + datetime.timedelta(weeks=endWeeks)


        #---- time, implement bi or weekly
        duration = datetime.timedelta(seconds = getDuration(df.iloc[i]['Time'])) # time object in seconds
        biWeekly = isBiWeekly(df.iloc[i]['Remark'])

        #---- venue
        venue = df.iloc[i]['Venue']

        #---- day, implement on start week
        dayInt = getDay(df.iloc[i]['Day'])
        startTime = getStartTime(df.iloc[i]['Time'])
        
        #---- if module start after recess week
        if getModuleStartWeek(df.iloc[i]['Remark']) > recessWeek:
            # just add after recess week
            addSecondHalf(cal, course, classType, title, indexNumber,\
                      duration, venue, endDate, biWeekly, startTime,\
                      startDate, recessWeek, dayInt, df.iloc[i]['Remark'])
            continue
        else: startDay = startDate + datetime.timedelta(weeks=getModuleStartWeek(df.iloc[i]['Remark'])-1, days=dayInt)
        startDay += datetime.timedelta(hours=startTime.hour, minutes=startTime.minute)
        
        #---- if module end before recess week
        if not afterRecessWeek:
            addFirstHalf(cal, course, classType, title, indexNumber, startDay, duration, venue, endDate, biWeekly)
            continue
        
        # ---- Add to event before recess week
        addFirstHalf(cal, course, classType, title, indexNumber, startDay, duration, venue, recessDate, biWeekly)

        # ---- Add to event after recess week
        addSecondHalf(cal, course, classType, title, indexNumber,\
                      duration, venue, endDate, biWeekly, startTime,\
                      startDate, recessWeek, dayInt, df.iloc[i]['Remark'])

    f = open('{}.ics'.format('calendar'), 'wb')
    f.write(cal.to_ical())
    f.close()

if __name__ == '__main__':
    createCalendar()