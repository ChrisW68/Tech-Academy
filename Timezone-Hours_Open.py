from datetime import datetime
from pytz import timezone

pacific = timezone('US/Pacific')
portland_time = datetime.now(pacific)
print portland_time.strftime('Portland, OR: %H:%M')
if portland_time.strftime('%H-%M')<'17:00' and \
   portland_time.strftime('%H-%M')>'09:00':
    print("Hello, Portland office is OPEN")
else:
    print("Sorry, Portland office is CLOSED")
                          
eastern = timezone('US/Eastern')
newyork_time = datetime.now(eastern)
print newyork_time.strftime('New York, NY: %H:%M')
if newyork_time.strftime('%H-%M')<'17:00' and \
   newyork_time.strftime('%H-%M')>'09:00':
    print("Hello, New York office is OPEN" )
else:
    print("Sorry, New York office is CLOSED")


europe = timezone('Europe/London')
london_time = datetime.now(europe)
print london_time.strftime('London, England: %H:%M')

if all([london_time.strftime('%H-%M')<'17:00', \
   london_time.strftime('%H-%M')>'09:00']):
    print("Hello, London office is OPEN" )
else:
    print("Sorry, London Office is closed")

