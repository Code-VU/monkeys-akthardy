
def monkeyCalculator(monkey_one,monkey_two):
        # This first line is provided for you
    smiling = False    
    if (monkey_one == 'y' or monkey_one == 'yes') and (monkey_two == 'y' or monkey_two == 'yes'):
        smiling =True
    elif (monkey_one == 'n' or monkey_one == 'no') and (monkey_two == 'n' or monkey_two == 'no'):
        smiling = True
    else:
        smiling = False
      
    if smiling == True:
        results = ("Uh oh! We're in trouble!")
    else:
        results = ("Yay! We're going to have a good day!") 
    return results    
    # end assignment

## if you want to test locally before you try to sync
## uncomment calculateTime() and run > python monkeyCalculator.py
## ***IMPORTANT*** please recomment before you submit/sync your assignment.
## OR YOUR TEST WILL NOT RUN
#monkey_one = input("Is the first monkey smiling?:  ").lower()
#monkey_two = input("Is the second monkey smiling?: ").lower()
#trouble = monkeyCalculator(monkey_one,monkey_two)
#print(trouble)