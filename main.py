import random
import hangman_art
import hangman_words


chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

#Print a logo:
print (hangman_art.logo)


#Create blanks
display = []
for _ in range(word_length):
    display += "_"
listOfGuesses = []

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    if (guess not in listOfGuesses):
        listOfGuesses += guess
    else:
        print ("You already tried this letter before!")   
        continue
    #If the user has entered a letter they've already guessed, print the letter and let them know.

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
       
        if letter == guess:
            display[position] = letter

    #Check if user is wrong.
    if guess not in chosen_word:
        print (f"The letter {guess} is not in the word")
        lives -= 1
        print (f"You have {lives} tries left!")
        if lives == 0:
            end_of_game = True
            print("You lose.")
            print (f"Your word was {chosen_word}")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(hangman_art.stages[lives])