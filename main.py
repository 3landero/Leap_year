def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return "Leap year."
      else:
        return "Not leap year."
    else:
      return "Leap year."
  else:
    return"Not leap year."

def days_in_month(year, month):
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  
  if month != 2:
    return month_days[month - 1]
  else:
    if is_leap_year == "Leap year.":
      print(is_leap_year)  
      return 29
    else:
      print("is not a leap year")  
      return 28  
  

year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
is_leap_year = is_leap(year)
days = days_in_month(year, month)
print(days)