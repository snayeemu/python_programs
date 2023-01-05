import datetime
from http.client import HTTP_VERSION_NOT_SUPPORTED
TodayDate = datetime.datetime.now()
print(TodayDate)
Year = TodayDate.strftime("%Y")
Month = TodayDate.strftime("%m")
Day = TodayDate.strftime("%d")
Hour= TodayDate.strftime("%H")
Minute= TodayDate.strftime("%M")
Second= TodayDate.strftime("%S")
print(Year)
FormattedDate = Day + "/" + Month + "/" + Year
print(FormattedDate)
Time = Hour + ":" + Minute + ":" + Second
print(Time)