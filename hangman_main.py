#hangman
import random

#import the list of names
from hangman_words import words
from hangmanLogo import logo,stages

print(logo)

#set the lives as 6
lives  = 6

#select the random word

chosen_word = random.choice(words)

word_length = len(chosen_word)

#crete the blanks for chosen word
blanks = ""
blanks+="_"*word_length
print(blanks)


#create the loop for number of guess
game_over = False
correct_words = []
while not game_over:
    #remember lives remaing
    print(f"you have {lives} left")
    #notice 
    if lives == 2:
        print(f"you have only {lives} lives guess carefull")

   
    #guess

    guess = input("guess the letter").lower()

     #check if the guess is repeated
    if guess in correct_words:
        print(f"you 've already guessed {guess} letter")

    #check the guess macthes to the chosen word

    display = "" # to store all items
    
    for letter in chosen_word:
        if letter == guess:
            display+=letter
            correct_words.append(letter)
        elif letter in correct_words:
            display+=letter  
        else:
            display+="_"  

    print(display)  
    #check the wrong words 
    if guess not in chosen_word:
        lives-=1
        if lives == 0:
            game_over = True
            print("************** you lose **************")

    if "_" not in display:
        game_over = True
        print("************** you win **************")

    print(stages[lives])    
#giveing right answer in the end

print(f"the right word is {chosen_word}")
