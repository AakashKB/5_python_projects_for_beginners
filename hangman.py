import random
incorrect_attempts = 0
letters_guessed = {} #Dict of letters gussed
word_bag = ["monster","person","vampire","werewolf","demon","donkey","lion","penguin","unicorn"] #list of words to choose from
word = random.choice(word_bag) #Chooses a rancom word from the list
answer = ["_" for i in range(len(word))] #Creates a blank array to store correct guesses by the user

while True:
    if incorrect_attempts >= 10:
        print("You're dead son, better luck next time.")
        break


    print("_________________________________________________________")
    print(f"Hidden word: {answer}")
    print(f"Guessed letters: {[key for key in letters_guessed.keys()]}") #Puts the keys of the dictionary into an array and prints it
    print(f"You have {10-incorrect_attempts} incorrect tries left.")
    guess=input("Guess letter or word> ").lower()

    if not guess.isalpha(): #Rules out any guesses with characters that are not alphabets
        print("Only letters allowed.")
    else:
        if len(guess) == 1:
            if guess in letters_guessed: #Checks if you have already guessed this character
                print("You have already tried to guess this letter.")
            else: 
                letters_guessed[guess] = True
                is_letter_in_word = False
                for i in range(len(word)): #Goes through the hidden word and populates it with the guessed letter if correct
                    if guess == word[i]:
                        is_letter_in_word = True
                        answer[i] = guess
                if is_letter_in_word:
                    print("Good guess!")
                else:
                    incorrect_attempts += 1
                    print("Try Again.")
        elif len(guess) == len(word): #Case where user tries to guess the whole word
            if guess == word:
                print(f"You won with {10 - incorrect_attempts} tries left!")
                break
            else:
                incorrect_attempts += 1
                print("Incorrect guess.")
        else:
            print("You can either guess one letter or the whole word")