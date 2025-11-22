correct = "12345" # stores the correct password "12345" under the variable 'correct'
attempts = 5 # stores 5 as the initial amount of attempts

while attempts > 0 : # continues the loop while the number of attempts are greater that 5
    pass_attempt = input("Please enter your password : ") # allows the user to input their password attempt
    
    if pass_attempt == correct :
        print ("Correct password entered !") # prints when the user has input the correct password

        break

    else: 
        attempts -= 1 # reduces the number of attempts by one if the wrong password is input
        print (f'Incorrect password entered, you have {attempts} left.\n') # prints when the wrong password is input

    if attempts == 0 :
        print("You have run out of attempts. Authorities have been alerted.") # prints when the user's number of attempts is 0
