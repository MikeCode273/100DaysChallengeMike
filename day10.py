#Still on functions, we dig deeper now
##functions with one return value
def format_name(f_name,l_name):
  formated_fname= f_name.title()
  formated_lname= l_name.title()
  return f"{formated_fname} {formated_lname}"

formated_text = format_name("micHael","fenTENg")
print(formated_text)


#function more then two return value
# def format_name(f_name,l_name):
#   if f_name=="" or l_name=="":
#     return f'wrong input'
#   formated_fname= f_name.title()
#   formated_lname= l_name.title()
#   return f"{formated_fname} {formated_lname}"

# formated_text = format_name(input("What's your first name? "),input("What's your last name? "))
# print(formated_text)

def is_leap(year):
  if year%4== 0:
    if year % 100 ==0:
      if year % 400 ==0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False
  
def days_in_month(year,month):
  if month<1 or month>12:
    return 'Invalid input'
  month_days = [32, 28, 31, 30, 31, 30, 31, 31, 30,31, 30, 31]
  if is_leap(year) and month==2:
    return 29
  return month_days[month-1]
  
  


days=days_in_month(int(input("Enter a year: ")),int(input("Enter a month: ")))
print(days)



