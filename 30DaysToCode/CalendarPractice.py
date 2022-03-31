"""
Calendar Practice 
Included here: Day 14 of 30 Days to Code.
See the Jupyter Notebook for more notes related to this tutorial.
"""

from datetime import datetime, date
import calendar

dateObj = date.today()
print('date object:',dateObj)
datetimeObj = datetime.now()
print('datetime object:',datetimeObj)

calObj = calendar.weekday(1994,9,7)
print('calendar object:',calendar.day_abbr[calObj])
