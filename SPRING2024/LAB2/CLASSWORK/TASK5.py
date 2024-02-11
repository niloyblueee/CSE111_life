#task5
def time_bomb(days):
  years=days//365
  day1=days%365
  months=day1//30
  day2=day1%30
  print(f'{years} years,{months} months and {day2} days')

time_bomb(4320)
time_bomb(4000)