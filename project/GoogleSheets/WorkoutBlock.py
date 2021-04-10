from project.config import *
from datetime import datetime, date

# Day Started = March 29 2021
startingDate = datetime.strptime("2021-03-29","%Y-%m-%d")
currentDate = datetime.strptime(str(date.today()),"%Y-%m-%d")
totalDays = abs((currentDate - startingDate).days)
currentWeekday = datetime.today().weekday()

# Starting column, go either 
startColumn = 2 # "B"
startRow = 3

def getRow():
    #Check if not weekend
    row = 11 * currentWeekday + 3
    if (currentWeekday > 4):
        row = 47 # Just get last day of the week 

    return row

# https://stackoverflow.com/questions/23861680/convert-spreadsheet-number-to-column-letter
def getColumn():
    column = startColumn + int(totalDays) - currentWeekday
    string = ""
    while column > 0:
        column, remainder = divmod(column - 1, 26)
        string = chr(65 + remainder) + string
    return string


# Sending emails needs to get past header which is why you need \n
def getDailyWorkout():
    goToLink = f"edit#gid={gid}&range={getColumn()}{getRow()}"
    fullLink = sbs_hypertrophy + goToLink
    return f"\nToday's workout: {fullLink}"