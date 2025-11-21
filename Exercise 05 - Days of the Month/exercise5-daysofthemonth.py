daysofmonth = { # stores months as keys and number of days as the values in a dictionary
    1 : 31,
    2 : 28,
    3 : 31,
    4 : 30,
    5 : 31,
    6 : 30,
    7 : 31,
    8 : 31,
    9 : 30,
    10 : 31,
    11 : 30,
    12 : 31
}

month = int(input("Please enter a number of a month : ")) # asks user to input a month number and converts it into an integer

if month in daysofmonth: # checks if the number input by the user is valid
  
  if month == 2:
    year = input("\nIs it a leap year? [ yes / no ] ") # asks the user whether it is a leap year or not

    if year.strip().lower() == "yes" : # adjusts the value when it is a leap year
      days = 29

    else:
      days = 28 # value remains the same if it is not a leap year

  else : 
    days = daysofmonth[month] # gives variable to the number of days to be used for the result
    
  print(f'\nIn month {month} there are {days} days. ') # prints out final result

else:
  
  print("\nPlease input a valid number of the month. [ 1 - 12 ] ") # printed if the value the user input is not valid
