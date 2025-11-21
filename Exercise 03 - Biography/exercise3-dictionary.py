name = input("Enter your name : ") # asks the user to input their name, two names can be given output remains the same.
hometown = input("Enter your hometown : ") # asks the user to input their hometown
age = input("Enter your age : ") # asks the user to input their age, age can be integer or string output remains the same.

bio = { # dictionary containing the user input data
    "name" : name,
    "hometown" : hometown,
    "age" : age, 
}

print("\nName : " , bio.get('name'), "\nHometown : " , bio.get('hometown'), "\nAge : ", bio.get('age'))
# prints all the values on separate lines
