import time

from dateutil.relativedelta import *
from dateutil.parser import *
from dateutil.tz import *
from datetime import timedelta, datetime


class DateHandler():
    def __init__(self, timeInfo):
        self.timeInfo = timeInfo
        self.dt = parse(timeInfo) - timedelta(hours=2) #adjusts to Brasilian Time -3 
     
    def getDate(self):
        year_str = str(self.dt.year)
        month_str = str(self.dt.month)
        day_str = str(self.dt.day)
        
        return '%s/%s/%s' %(day_str, month_str,year_str)

    
    def getTime(self):
        if self.dt.hour < 10:
            hour_str = '0'+str(self.dt.hour)
        else:
            hour_str = str(self.dt.hour)
    
        if self.dt.minute < 10:
            minutes_str = '0'+str(self.dt.minute)
        else:
            minutes_str = str(self.dt.minute)
    
    
        if self.dt.second < 10:
            seconds_str = '0'+str(self.dt.second)
        else:
            seconds_str = str(self.dt.second) 
    
        return '%s:%s:%s' %(hour_str, minutes_str, seconds_str)
    
    # checks if given time is     
    def timeDiffHour(self,timeToCheck):
        FMT = '%H:%M:%S'
        tdelta = datetime.strptime('01:07:00', FMT) - datetime.strptime(timeToCheck, FMT)
        x = time.strptime(str(tdelta),FMT)
        seconds = timedelta(hours=x.tm_hour,minutes=x.tm_min,seconds=x.tm_sec).total_seconds()
        if seconds / 3600 >= 1:
            return True
        return False   
        
# This function must check if a given date and time are inside a period datetime. If the tolerance is bigger than 0 means that the period time is dilated.
def fitTime(initialDateTime, durationTime,  givenTime, toleranceInMinutes):
   
    #gets the initial timestamp
    initial_timestamp = time.mktime(datetime.strptime(initialDateTime, "%d/%m/%Y - %H:%M:%S").timetuple())
    
    #converts givenTime to seconds
    x = time.strptime(durationTime,'%H:%M:%S')
    givenTime_seconds = timedelta(hours=x.tm_hour,minutes=x.tm_min,seconds=x.tm_sec).total_seconds()

    #calculates the endtime according the durationtime
    endDateTime = parse(initialDateTime) + timedelta(seconds=givenTime_seconds)
    
    #gets the end timestamp
    endDateTime_timestamp = time.mktime(datetime.strptime(str(endDateTime), "%Y-%m-%d  %H:%M:%S").timetuple()) 
    
    #if this value is bigger than 0 means that the givenTime can be in bigger interval 
    if toleranceInMinutes > 0:
        initial_timestamp -= toleranceInMinutes * 60
        endDateTime_timestamp += toleranceInMinutes * 60
    
    #gets the given timestamp
    givenDateTime_timestamp  = time.mktime(datetime.strptime(givenTime, "%d/%m/%Y - %H:%M:%S").timetuple())

    if initial_timestamp <= givenDateTime_timestamp and givenDateTime_timestamp <= endDateTime_timestamp:
        return True
     
    return False

# Uses...

#twitter_time = 'Tue Oct 22 22:08:29 +0000 2013'
#format_date = '22/10/2013'
#format_time = 'hh:mm:ss'
#time_now = DateHandler(twitter_time)
#print 'date:', time_now.getDate()
#print 'time:', time_now.getTime()
#print fitTime('22/10/2013 - 19:08:29', '01:20:00', '22/10/2013 - 21:15:29', 60)



