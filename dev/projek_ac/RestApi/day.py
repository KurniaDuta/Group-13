import datetime
import time
import calendar

def result_day(service):
    result = 0
    x = service.split("/")
    localtime = time.localtime(time.time())
    current_day = localtime.tm_yday
    current_year = localtime.tm_year
    date = datetime.datetime(int(x[2]), int(x[1]), int(x[0]))
    strc_time =  date.timetuple()
    y_day = strc_time.tm_yday
    if int(x[2]) != current_year:
        difference = current_year - int(x[2]) - 1
        temp_year = int(x[2])
        if calendar.isleap(temp_year):
            result = 366 - y_day
        else :
            result = 365 - y_day
        for i in range(difference):
            if calendar.isleap(temp_year):
                result = result + 366
            else :
                result = result + 365
        result = result + current_day
    else :
        result = current_day - y_day
    return str(result) + " hari"

    