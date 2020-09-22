import random

print("Welcome to guess the number!")

#Infinite loop to keep the game running forever
while True:
    print("I am thinking of a number between 1 and 100, try guessing what it is");
    #Picks a ranodm number between 1 and 100, it does not include 101
    number = random.randrange(1,101)

    #variable to keep track of the total number of guesses the user makes
    tries = 0

    #Infinite loop to allow the user to keep guessing until they get it right
    while True:
        guess = int(input("Your Guess > "))
        tries += 1

        #Conditional logic to check if user's guess is higher or lower than chosen number
        if guess == number:
            #Formatted string, `{tries}` prints the variable
            print(f'You won in {tries} tries!')
            break
        elif guess < number:
            print("The number I'm thinking of is higher, try again!")
        elif guess > number:
            print("The number I'm thinking of is lower, try again!")
