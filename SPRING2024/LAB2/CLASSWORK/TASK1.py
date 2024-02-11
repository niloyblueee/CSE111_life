#task1
def BMIcalc(height,weight):
  height=height/100
  bmi=round(weight/(height**2),1)
  if bmi<18.5:
    x='Underweight'
  elif 18.5<=bmi<=24.9:
    x='Normal'
  elif 25<=bmi<=30:
    x='Overweight'
  else:
    x='Obese'

  print(f'Score is {bmi}. You are {x}')


BMIcalc(175,96)
BMIcalc(152,48)
