capitals = { # stores 10 country names and capitals in a dicionary
    'France' : 'Paris',
    'Germany' : 'Berlin',
    'Greece' : 'Athens',
    'Belgium' : 'Brussels',
    'Italy' : 'Rome',
    'Hungary' : 'Budapest',
    'Azerbaijan' : 'Baku',
    'Austria' : 'Vienna',
    'Romania' : 'Bucharest',
    'Netherlands' : 'Amsterdam'
}

for country, capital in capitals.items(): # uses for loop to loop through the key-value pairs in the dictionary
    answer = input(f'What is the capital of {country} ? ') # user is asked to answer for the capital name

    if answer.strip().lower() == capital.lower(): # lowercase versions of the answer are taken so the quiz is not case-sensitive
        print("Correct answer! \n") # tells the user when their answer is correct.
    
    else: 
        print("Incorrect answer. \n") # tells the user when their answer is wrong.
