#leap year
def isleapyear(year):
  if(year%4==0and year%400!=0)or year%400==0:
    return True
  else: 
    return False
year=2024
if isleapyear(year):
  print('{} is a leap year.'.format(year))
else:
  print('{} is a leap year.'.format(year))
