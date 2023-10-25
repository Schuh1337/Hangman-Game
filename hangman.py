import random
import os
import time
words = ["elephant", "sunshine", "basketball", "pineapple", "rainbow", "butterfly", "meditation", "telescope", "strawberry", "zucchini", "adventure", "waterfall", "universe", "celebration", "octopus", "firefly", "reflection", "labyrinth", "marshmallow", "symphony", "midnight", "hummingbird", "skyscraper", "broccoli", "waterfall", "giraffe", "chocolate", "ocean", "bicycle", "piano", "mountain", "galaxy", "seashell", "dragonfly", "candle", "penguin", "wanderlust", "constellations", "cappuccino", "serendipity", "enchantment", "tranquility", "aurora", "kaleidoscope", "wanderer", "moonlight", "serenity", "starlight", "nostalgia", "infinity"]
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
def choose_word():
    return random.choice(words)
def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display
def display_hangman(attempts):
    stages = [
        '''
           _________
           |/      |
           |     
           |     
           |    
           |   
        ''',
        '''
           _________
           |/      |
           |      (_)
           |      
           |    
           |   
        ''',
        '''
           _________
           |/      |
           |      (_)
           |       |
           |    
           |   
        ''',
        '''
           _________
           |/      |
           |      (_)
           |       |/
           |    
           |   
        ''',
        '''
           _________
           |/      |
           |      (_)
           |      /|\\
           |    
           |   
        ''',
        '''
           _________
           |/      |
           |      (_)
           |      /|\\
           |      / 
           |   
        ''',
        '''
           _________
           |/      |
           |      (_)
           |      /|\\
           |      / \\
           |   
        '''
    ]

    print(stages[6 - attempts])
def hangman():
    word_to_guess = choose_word()
    guessed_letters = []
    attempts = 6
    while attempts > 0:
        clear_screen()
        display_hangman(attempts)
        print(f">>     {display_word(word_to_guess, guessed_letters)}\n\n")
        print("/ Attempts left:", attempts)
        print("/ Guessed letters:", ", ".join(guessed_letters))
        guess = input("/ Guess a letter: ").lower()
        if len(guess) != 1 or not guess.isalpha():
            print("/ Please guess a single and valid letter.")
            time.sleep(1.5)
            continue
        if guess in guessed_letters:
            print("/ You've already guessed that letter.")
            time.sleep(1.5)
            continue
        guessed_letters.append(guess)
        if guess in word_to_guess:
            pass
        else:
            attempts -= 1
        if "_" not in display_word(word_to_guess, guessed_letters):
            clear_screen()
            display_hangman(attempts)
            print("/ Congratulations! You've guessed the word:", word_to_guess)
            break
    if attempts == 0:
        clear_screen()
        display_hangman(attempts)
        print("/ You're out of attempts. The word was:", word_to_guess)
    play_again = input("/ Play again? (y/n): ").lower()
    if play_again == "y":
        hangman()
hangman()
