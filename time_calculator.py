import datetime


def add_time(start, duration, weekDay=''):
  
  startTime = datetime.datetime.strptime(start, "%I:%M %p")
  durationDateime = datetime.timedelta(hours=int(duration.split(':')[0]),
                                       minutes=int(duration.split(':')[1]))

  overTime = startTime + durationDateime
  
  returnTime = overTime.strftime("%I:%M %p")[1:] if overTime.strftime(
    "%I:%M %p")[0] == '0' else overTime.strftime("%I:%M %p")
  daysPassed = int(overTime.strftime("%d")) - 1
  
  strDaysPassed = f' ({daysPassed} days later)' if (
    daysPassed) > 1 else ' (next day)' if (daysPassed) == 1 else ''
  
  if weekDay:
    weekDay = weekDay.lower()
    weekList = [
      'monday', 'tuesday', 'wednesday', 'thurday', 'friday', 'saturday',
      'sunday'
    ]
    weekDayIndex = weekList.index(weekDay)
    newDay = f', {str(weekList[(daysPassed%7+weekDayIndex)%7]).capitalize()}'

  return f"{returnTime}{strDaysPassed}" if not weekDay else f"{returnTime}{newDay}{strDaysPassed}"
