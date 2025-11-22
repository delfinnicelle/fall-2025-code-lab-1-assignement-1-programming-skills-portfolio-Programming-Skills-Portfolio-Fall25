names = [ "Jake", "Zac", "Ian", "Ron", "Sam", "Dave" ] # stores names in a list

namesearch = input("Please enter a name you want to search for : ") # asks the user to input a name

namefound = False # a flag to if the name is found

for name in names : # loop through the names in the list
   if name.lower() == namesearch.lower() : 

    namefound = True # changes flag if name is found
    break # exits loop
   
if namefound == True:
   print (f'{name} is in the list !') # prints if the name was found in the list with the loop

else:
   print(f'{namesearch} is not in the list.') # prints if name was not found in the list with the loop
