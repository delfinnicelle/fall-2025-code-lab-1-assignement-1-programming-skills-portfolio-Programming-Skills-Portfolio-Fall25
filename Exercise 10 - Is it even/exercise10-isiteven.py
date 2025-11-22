def even_or_odd(num) : # defines the function even_or_odd
  
  if num % 2 == 0 : # finds out if the number is even by using the modulo operator
    return f'{num} is an even number !\n' # returns the message if the number is even

  else :
    return f'{num} is an odd number !\n' # returns the message if the number is odd

def main() : # defines the main function
  
  while True :
   # asks the user to input a number
   user_num = input("Please enter a number to check if it is even or odd : ")
    
   if user_num.isdigit() : # checks if the input is only digits
     user_num = int(user_num) # converts the string input into integer
     print(even_or_odd(user_num)) # calls the odd_or_even function and prints it to the user
     break # stops the loop
  
   else : # function loops if non-integer is input
     # prints if the input is does not contain digits
     print("Input is not an integer. Please enter a whole number only. \n") 

main() # calls the main function
