import random

#List of possible answer the 8 ball can choose from
potential_answers = ['yes','no','maybe','try again later',
                     'you wish','100% yes','no freaking way']

print("Welcome to the Magic 8 Ball")

#Infinite loop to keep the game running forever
while True:
    #Asks user for input, no need to store it
    input("Ask a yes or no question > ")

    #Choose a random number between 0 and the length of the answers list
    rand_num = random.randrange(len(potential_answers))
    
    #Use random number as index to pick a response from the answers list
    response = potential_answers[rand_num]
    
    print(response)
