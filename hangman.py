import random
from pyfiglet import Figlet

figlet = Figlet()
#adding fonts from library to list
fonts = figlet.getFonts()

def main():
#prompt to welcome the user to the game
    prompt = "Welcome to Hangman, Enjoy ;)"
    print(font_display(prompt))
    #word selection
    game_word = word_choice()
    #find the length of the chosen word to output the amount of dashes to the game
    output = []
    i = 0
    while i < (len(game_word)-1):
        output += "_"
        i += 1
    print("   ".join(output))
    print(f"{len(game_word) - 1} LETTERS")
    print(gameplay(output, game_word))

def word_choice(): 
    #create a list of words that would be randomly selected
    game_words = []
    with open("words.txt", "r") as file:
        for word in file:
            game_words.append(word)
    #word is set to be randomly chosen from list
    random_num = random.randint(0, (len(game_words))- 1)
    game_word = game_words[random_num]
    return game_word 

#display
def font_display(word):
    figlet.setFont(font="banner")
    return figlet.renderText(word)

#gameplay
def gameplay(output, game_word):
    letter_check = []
    # user starts with 7 lives
    lives = 7
    #prompt the user to input letters 
    while True:
        #takes in user input
        user_input = input("Enter a letter: ").lower()
        if len(user_input) > 1:
            print("Enter a letter, not word")
        #check to confirm input is a letter
        if user_input.isalpha() == True:
            for i in range(len(game_word)):
                letter = game_word[i]
                #compares if user input matches a letter in the word
                if letter == user_input:
                    output[i] = user_input
            print("   ".join(output))
            # print(drawing(lives))
            if user_input not in game_word:
                lives -= 1
                print(drawing(lives))
                if lives == 0:
                    break
            if "_" not in output:
                figlet.setFont(font="banner")
                return figlet.renderText("You Win!")
        else:
            print("Enter a letter please")
    print(game_word)
    figlet.setFont(font="banner")
    return figlet.renderText("You Lose!")

#hangman tracker drawing
def drawing(lives):
    if lives == 6:
        return '''
  +---+
  |   |
      |
      |
      |
      |
=========
''' 
    elif lives == 5:
        return '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''' 
    elif lives == 4:
        return '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''' 
    elif lives == 3:
        return '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''' 
    elif lives == 2:
        return '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''' 
    elif lives == 1:
        return '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
'''
    else:
        return '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
'''



if __name__ == "__main__":
    main()