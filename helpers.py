import datetime

#---- Obtain class type
def getClassType(classTypeString):
    return classTypeString

#---- Obtain group
def getGroup(groupString):
    return groupString

#---- day
def getDay(dayString):
    # Convert date into integer
    dayDict = {'MON' : 0, 'TUE' : 1, 'WED' : 2, 'THU' : 3, 'FRI' : 4, 'SAT' : 5}
    return dayDict[dayString]

#---- time
def getDuration(timeString):
    timestamp1 = datetime.datetime.strptime(timeString.split('-')[0],"%H%M")
    timestamp2 = datetime.datetime.strptime(timeString.split('-')[1],"%H%M")
    return (timestamp2 - timestamp1).total_seconds()

def getStartTime(timeString):
    return datetime.datetime.strptime(timeString.split('-')[0],"%H%M")

#---- venue
def getVenue(venueString):
    return venueString

def getModuleStartWeek(remark):
    # find starting week
    return int(remark[remark.find('Wk')+2])

def isBiWeekly(remark):
    # find if there are any commas
    if remark.count(',')>2: # bi-weekly schedule
        return True
    return False

def isEvenWeek(remark):
    if all(x in remark for x in ['2','4']):
        return True
    return False

def getModuleEndWeek(remark):
    # find out last day by spliting through comma or hyphen
    if ',' in remark:
        try:
            return int(remark.split(',')[-1])
        except:
            return int(remark.split(',')[-1][-1]) 
    else:
        try:
            return int(remark.split('-')[-1])
        except:
            return int(remark.split('-')[-1][-1])