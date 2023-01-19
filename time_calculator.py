import datetime


def add_time(start, duration, weekDay=''):
  print(start)
  print(duration)
  print(weekDay)
  weekDay = weekDay.lower()
  # daysPassed = math.floor(int(duration.split(':')[0]) / 24)

  # print(daysPassed, ' daysPassed')
  startTime = datetime.datetime.strptime(start, "%I:%M %p")
  print(startTime, ' startTime')

  # h = duration.split(':')[0]
  # m = duration.split(':')[1]
  # print(h, ' h')
  # print(m, ' m')

  # t = datetime.time(hour= int(duration.split(':')[0]), minute = int(duration.split(':')[1]))
  # t = datetime.datetime.strptime(duration, "%H:%M")
  durationDateime = datetime.timedelta(hours=int(duration.split(':')[0]),
                                       minutes=int(duration.split(':')[1]))
  print(durationDateime, ' durationDateime')

  overTime = startTime + durationDateime
  print(overTime, ' sum')
  returnTime = overTime.strftime("%I:%M %p")[1:] if overTime.strftime(
    "%I:%M %p")[0] == '0' else overTime.strftime("%I:%M %p")
  daysPassed = int(overTime.strftime("%d")) - 1
  print(daysPassed)
  strDaysPassed = f' ({daysPassed} days later)' if (
    daysPassed) > 1 else ' (next day)' if (daysPassed) == 1 else ''
  if weekDay:
    print(daysPassed % 7)
    weekList = [
      'monday', 'tuesday', 'wednesday', 'thurday', 'friday', 'saturday',
      'sunday'
    ]
    weekDayIndex = weekList.index(weekDay)
    print((daysPassed % 7 + weekDayIndex) % 7)
    newDay = f', {str(weekList[(daysPassed%7+weekDayIndex)%7]).capitalize()}'
    print(newDay)

  print('-' * 20)
  return f"{returnTime}{strDaysPassed}" if not weekDay else f"{returnTime}{newDay}{strDaysPassed}"
