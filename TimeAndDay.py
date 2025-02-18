import datetime

# This module merely provides the current time and day for the program.

currentTime = datetime.datetime.now()
currentDay = currentTime.strftime("%A")