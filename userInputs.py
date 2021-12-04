import datetime

def getUserInputs():
    startDate = input("Please input the date (Monday) of the first week of school in the format (ddmmyyyy): ")
    startDateVerify = input("Please input the date (Monday) of the first week of school in the format (ddmmyyyy) to double confirm: ")
    startDate = datetime.datetime.strptime(startDate, "%d%m%Y")
    
    totalWeeks = input("Please input number of teaching weeks (not counting recess week): ")
    totalWeeks = validateInt(totalWeeks, "Please input number of teaching weeks (not counting recess week): ")
    
    recessWeek = input("Please input the week your recess week falls on (week before recess week + 1): ")
    recessWeek = validateInt(recessWeek, "Please input the week your recess week falls on (week before recess week + 1): ")
    recessWeek = int(recessWeek) -1
    recessDate = startDate + datetime.timedelta(weeks=recessWeek)
    
    return startDate, int(totalWeeks), recessWeek, recessDate

def validateInt(item, statement):
    while not item.isdigit():
        print("Invalid input, please input an integer")
        item = input(statement)
    return item