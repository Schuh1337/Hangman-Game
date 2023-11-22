import random
import os
import time
import sys
words = ["elephant", "sunshine", "basketball", "pineapple", "rainbow", "butterfly", 
    "meditation", "telescope", "strawberry", "zucchini", "adventure", "waterfall", 
    "universe", "celebration", "octopus", "firefly", "reflection", "labyrinth", 
    "marshmallow", "symphony", "midnight", "hummingbird", "skyscraper", "broccoli", 
    "waterfall", "giraffe", "chocolate", "ocean", "bicycle", "piano", "mountain", 
    "galaxy", "seashell", "dragonfly", "candle", "penguin", "wanderlust", "constellations", 
    "cappuccino", "serendipity", "enchantment", "tranquility", "aurora", "kaleidoscope", 
    "wanderer", "moonlight", "serenity", "starlight", "nostalgia", "infinity", "jungle", 
    "wonder", "mystic", "whisper", "sapphire", "gentle", "effervescent", "cascade", "harmony", 
    "vibrant", "echo", "paradise", "breeze", "twilight", "mysterious", "whimsical", "velvet", 
    "enchanted", "glistening", "lullaby", "whirlwind", "flourish", "melody", "enigma", 
    "celestial", "eternity", "whisper", "sparkle", "blossom", "inspiration", "captivate", 
    "shimmer", "glow", "luminous", "captivating", "intuition", "majestic", "resonate", "crystal", 
    "inspire", "mesmerize", "adventure", "perfection", "paradise", "miracle", "fantasy", "charisma", 
    "ecstasy", "serendipity", "wanderlust", "labyrinth", "phenomenal", "wonderment", "enthusiasm", 
    "imagination", "whimsy", "fascination", "harmonious", "illuminated", "spellbound", "eclectic", 
    "brilliance", "exploration", "magnificent", "unforgettable", "enigmatic", "euphoria", "tranquil",
    "radiant", "serenity", "elegant", "rhapsody", "adventure", "harmony", "dreamscape", "ethereal",
    "captivating", "effulgent", "paradox", "breathtaking", "enchanting", "mellifluous", "captivation",
    "fantasia", "enchant", "divine", "idyllic", "lighthearted", "splendor", "iridescent", "surreal",
    "astounding", "utopia", "infinite", "verdant", "luminescent", "harbor", "beauty", "liberty", "cheer",
    "brio", "carnival", "jovial", "lively", "rejoice", "melodic", "jubilation", "idyllic", "panorama",
    "tranquil", "prosperity", "bliss", "glimmer", "gala", "quixotic", "celestial", "imagination", "zephyr",
    "zenith", "seraphic", "tempest", "mystique", "jocund", "sonorous", "intrepid", "ebullient", "ethereal",
    "nostalgic", "gratitude", "charismatic", "scintillate", "luminosity", "effulgence", "epiphany", "pinnacle",
    "captivation", "reflection", "lighthearted", "marvel", "enigmatic", "quiescent", "serendipitous",
    "effervesce", "imagine", "mellifluous", "blissful", "resonate", "enthralling", "mystical", "tranquility",
    "eternity", "rhapsody", "perennial", "dreamscape", "harmonious", "labyrinth", "exuberance", "vivid",
    "inspiration", "wanderlust", "illustrious", "oasis", "synchronicity", "ecstasy", "mesmerize",
    "universe", "zephyr", "eclectic", "serenity", "serendipity", "luminous", "jubilation", "paradise",
    "whimsical", "breathtaking", "adventure", "celebration", "magnificent", "cascade", "lullaby",
    "effervescent", "captivate", "fantasy", "phenomenal", "majestic", "inspire", "twinkle", "harmony",
    "imagination", "euphoria", "whisper", "paradox", "mesmerize", "wonderment", "charisma", "mystic",
    "moonlight", "brilliance", "perfection", "whimsy", "miracle", "harbor", "whirlwind", "zenith",
    "sapphire", "iridescent", "lighthearted", "glistening", "harmonize", "radiance", "enthusiasm",
    "labyrinth", "resplendent", "serenity", "divine", "seraphic", "melodic", "gentle", "effulgent",
    "unforgettable", "enchantment", "wonder", "prosperity", "lively", "mysterious", "gratitude", "imagine",
    "ethereal", "whisper", "celestial", "mellifluous", "glow", "serendipitous", "marvel", "sparkle",
    "surreal", "jovial", "captivating", "mesmerize", "mystique", "triumph", "captivation", "ethereal",
    "idyllic", "splendor", "brio", "fantasia", "zenith", "enigmatic", "breathtaking", "ecstasy",
    "serendipity", "whimsical", "whirlwind", "enchantment", "captivating", "luminosity", "serenity",
    "seraphic", "majestic", "imagination", "lighthearted", "gala", "zephyr", "vivid", "luminous",
    "exuberance", "blissful", "tranquility", "mystical", "eclectic", "serenity", "enigmatic", "zenith",
    "eternity", "rhapsody", "wanderlust", "prosperity", "vibrant", "paradise", "serendipity", "breeze",
    "twilight", "mysterious", "whimsical", "velvet", "enchanted", "glistening", "lullaby", "whirlwind",
    "flourish", "melody", "enigma", "celestial", "eternity", "whisper", "sparkle", "blossom",
    "inspiration", "captivate", "shimmer", "glow", "luminous", "captivating", "intuition", "majestic",
    "resonate", "crystal", "inspire", "mesmerize", "adventure", "perfection", "paradise", "miracle",
    "fantasy", "charisma", "ecstasy", "serendipity", "wanderlust", "labyrinth", "phenomenal",
    "wonderment", "enthusiasm", "imagination", "whimsy", "fascination", "harmonious", "illuminated",
    "spellbound", "eclectic", "brilliance", "exploration", "magnificent", "unforgettable", "enigmatic",
    "euphoria", "tranquil", "radiant", "serenity", "elegant", "rhapsody", "adventure", "harmony",
    "dreamscape", "ethereal", "captivating", "effulgent", "paradox", "breathtaking", "enchanting",
    "mellifluous", "captivation", "fantasia", "enchant", "divine", "idyllic", "lighthearted", "splendor",
    "iridescent", "surreal", "astounding", "utopia", "infinite", "verdant", "luminescent", "harbor",
    "beauty", "liberty", "cheer", "brio", "carnival", "jovial", "lively", "rejoice", "melodic",
    "jubilation", "idyllic", "panorama", "tranquil", "prosperity", "bliss", "glimmer", "gala",
    "quixotic", "celestial", "imagination", "zephyr", "zenith", "seraphic", "tempest", "mystique",
    "jocund", "sonorous", "intrepid", "ebullient", "ethereal", "nostalgic", "gratitude", "charismatic",
    "scintillate", "luminosity", "effulgence", "epiphany", "pinnacle", "captivation", "reflection",
    "lighthearted", "marvel", "enigmatic", "quiescent", "serendipitous", "effervesce", "imagine",
    "mellifluous", "blissful", "resonate", "enthralling", "mystical", "tranquility", "eternity",
    "rhapsody", "perennial", "dreamscape", "harmonious", "labyrinth", "exuberance", "vivid",
    "inspiration", "wanderlust", "illustrious", "oasis", "synchronicity", "ecstasy", "mesmerize",
    "universe", "zephyr", "eclectic", "serenity", "serendipity", "luminous", "jubilation", "paradise",
    "whimsical", "breathtaking", "adventure", "celebration", "magnificent", "cascade", "lullaby",
    "effervescent", "captivate", "fantasy", "phenomenal", "majestic", "inspire", "twinkle", "harmony",
    "imagination", "euphoria", "whisper", "paradox", "mesmerize", "wonderment", "charisma", "mystic",
    "moonlight", "brilliance", "perfection", "whimsy", "miracle", "harbor", "whirlwind", "zenith",
    "sapphire", "iridescent", "lighthearted", "glistening", "harmonize", "radiance", "enthusiasm",
    "labyrinth", "resplendent", "serenity", "divine", "seraphic", "melodic", "gentle", "effulgent",
    "unforgettable", "enchantment", "wonder", "prosperity", "lively", "mysterious", "gratitude", "imagine",
    "ethereal", "whisper", "celestial", "mellifluous", "glow", "serendipitous", "marvel", "sparkle",
    "surreal", "jovial", "captivating", "mesmerize", "mystique", "triumph", "captivation", "ethereal",
    "idyllic", "splendor", "brio", "fantasia", "zenith", "enigmatic", "breathtaking", "ecstasy",
    "serendipity", "whimsical", "whirlwind", "enchantment", "captivating", "luminosity", "serenity",
    "serendipity", "luminous", "majestic", "imagination", "lighthearted", "gala", "zephyr", "vivid",
    "luminous", "exuberance", "blissful", "tranquility", "mystical", "eclectic", "serenity", "enigmatic",
    "zenith", "eternity", "rhapsody", "wanderlust", "prosperity", "vibrant", "paradise", "serendipity",
    "breeze", "twilight", "mysterious", "whimsical", "velvet", "enchanted", "glistening", "lullaby",
    "whirlwind", "flourish", "melody", "enigma", "celestial", "eternity", "whisper", "sparkle", "blossom",
    "inspiration", "captivate", "shimmer", "glow", "luminous", "captivating", "intuition", "majestic",
    "resonate", "crystal", "inspire", "mesmerize", "adventure", "perfection", "paradise", "miracle",
    "fantasy", "charisma", "ecstasy", "serendipity", "wanderlust", "labyrinth", "phenomenal", "wonderment",
    "enthusiasm", "imagination", "whimsy", "fascination", "harmonious", "illuminated", "spellbound",
    "eclectic", "brilliance", "exploration", "magnificent", "unforgettable", "enigmatic", "euphoria",
    "tranquil", "radiant", "serenity", "elegant", "rhapsody", "adventure", "harmony", "dreamscape", "ethereal",
    "captivating", "effulgent", "paradox", "breathtaking", "enchanting", "mellifluous", "captivation",
    "fantasia", "enchant", "divine", "idyllic", "lighthearted", "splendor", "iridescent", "surreal",
    "astounding", "utopia", "infinite", "verdant", "luminescent", "harbor", "beauty", "liberty", "cheer",
    "brio", "carnival", "jovial", "lively", "rejoice", "melodic", "jubilation", "idyllic", "panorama",
    "tranquil", "prosperity", "bliss", "glimmer", "gala", "quixotic", "celestial", "imagination", "zephyr",
    "zenith", "seraphic", "tempest", "mystique", "jocund", "sonorous", "intrepid", "ebullient", "ethereal",
    "nostalgic", "gratitude", "charismatic", "scintillate", "luminosity", "effulgence", "epiphany", "pinnacle",
    "captivation", "reflection", "lighthearted", "marvel", "enigmatic", "quiescent", "serendipitous",
    "effervesce", "imagine", "mellifluous", "blissful", "resonate", "enthralling", "mystical", "tranquility",
    "eternity", "rhapsody", "perennial", "dreamscape", "harmonious", "labyrinth", "exuberance", "vivid",
    "inspiration", "wanderlust", "illustrious", "oasis", "synchronicity", "ecstasy", "mesmerize",
    "universe", "zephyr", "eclectic", "serenity", "serendipity", "luminous", "jubilation", "paradise",
    "whimsical", "breathtaking", "adventure", "celebration", "magnificent", "cascade", "lullaby",
    "effervescent", "captivate", "fantasy", "phenomenal", "majestic", "inspire", "twinkle", "harmony",
    "imagination", "euphoria", "whisper", "paradox", "mesmerize", "wonderment", "charisma", "mystic",
    "moonlight", "brilliance", "perfection", "whimsy", "miracle", "harbor", "whirlwind", "zenith",
    "sapphire", "iridescent", "lighthearted", "glistening", "harmonize", "radiance", "enthusiasm",
    "labyrinth", "resplendent", "serenity", "divine", "seraphic", "melodic", "gentle", "effulgent",
    "unforgettable", "enchantment", "wonder", "prosperity", "lively", "mysterious", "gratitude", "imagine",
    "ethereal", "whisper", "celestial", "mellifluous", "glow", "serendipitous", "marvel", "sparkle",
    "surreal", "jovial", "captivating", "mesmerize", "mystique", "triumph", "captivation", "ethereal",
    "idyllic", "splendor", "brio", "fantasia", "zenith", "enigmatic", "breathtaking", "ecstasy",
    "serendipity", "whimsical", "whirlwind", "enchantment", "captivating", "luminosity", "serenity",
    "serendipity", "luminous", "majestic", "imagination", "lighthearted", "gala", "zephyr", "vivid",
    "luminous", "exuberance", "blissful", "tranquility", "mystical", "eclectic", "serenity", "enigmatic",
    "zenith", "eternity", "rhapsody", "wanderlust", "prosperity", "vibrant", "paradise", "serendipity",
    "breeze", "twilight", "mysterious", "whimsical", "velvet", "enchanted", "glistening", "lullaby",
    "whirlwind", "flourish", "melody", "enigma", "celestial", "eternity", "whisper", "sparkle", "blossom",
    "inspiration", "captivate", "shimmer", "glow", "luminous", "captivating", "intuition", "majestic",
    "resonate", "crystal", "inspire", "mesmerize", "adventure", "perfection", "paradise", "miracle",
    "fantasy", "charisma", "ecstasy", "serendipity", "wanderlust", "labyrinth", "phenomenal", "wonderment",
    "enthusiasm", "imagination", "whimsy", "fascination", "harmonious", "illuminated", "spellbound",
    "eclectic", "brilliance", "exploration", "magnificent", "unforgettable", "enigmatic", "euphoria",
    "tranquil", "radiant", "serenity", "elegant", "rhapsody", "adventure", "harmony", "dreamscape", "ethereal",
    "captivating", "effulgent", "paradox", "breathtaking", "enchanting", "mellifluous", "captivation",
    "fantasia", "enchant", "divine", "idyllic", "lighthearted", "splendor", "iridescent", "surreal",
    "astounding", "utopia", "infinite", "verdant", "luminescent", "harbor", "beauty", "liberty", "cheer",
    "brio", "carnival", "jovial", "lively", "rejoice", "melodic", "jubilation", "idyllic", "panorama",
    "tranquil", "prosperity", "bliss", "glimmer", "gala", "quixotic", "celestial", "imagination", "zephyr",
    "zenith", "seraphic", "tempest", "mystique", "jocund", "sonorous", "intrepid", "ebullient", "ethereal",
    "nostalgic", "gratitude", "charismatic", "scintillate", "luminosity", "effulgence", "epiphany", "pinnacle",
    "captivation", "reflection", "lighthearted", "marvel", "enigmatic", "quiescent", "serendipitous",
    "effervesce", "imagine", "mellifluous", "blissful", "resonate", "enthralling", "mystical", "tranquility",
    "eternity", "rhapsody", "perennial", "dreamscape", "harmonious", "labyrinth", "exuberance", "vivid",
    "inspiration", "wanderlust", "illustrious", "oasis", "synchronicity", "ecstasy", "mesmerize",
    "universe", "zephyr", "eclectic", "serenity", "serendipity", "luminous", "jubilation", "paradise",
    "whimsical", "breathtaking", "adventure", "celebration", "magnificent", "cascade", "lullaby",
    "effervescent", "captivate", "fantasy", "phenomenal", "majestic", "inspire", "twinkle", "harmony",
    "imagination", "euphoria", "whisper", "paradox", "mesmerize", "wonderment", "charisma", "mystic",
    "moonlight", "brilliance", "perfection", "whimsy", "miracle", "harbor", "whirlwind", "zenith",
    "sapphire", "iridescent", "lighthearted", "glistening", "harmonize", "radiance", "enthusiasm",
    "labyrinth", "resplendent", "serenity", "divine", "seraphic", "melodic", "gentle", "effulgent",
    "unforgettable", "enchantment", "wonder", "prosperity", "lively", "mysterious", "gratitude", "imagine",
    "ethereal", "whisper", "celestial", "mellifluous", "glow", "serendipitous", "marvel", "sparkle",
    "surreal", "jovial", "captivating", "mesmerize", "mystique", "triumph", "captivation", "ethereal",
    "idyllic", "splendor", "brio", "fantasia", "zenith", "enigmatic", "breathtaking", "ecstasy",
    "serendipity", "whimsical", "whirlwind", "enchantment", "captivating", "luminosity", "serenity",
    "serendipity", "luminous", "majestic", "imagination", "lighthearted", "gala", "zephyr", "vivid",
    "luminous", "exuberance", "blissful", "tranquility", "mystical", "eclectic", "serenity", "enigmatic",
    "zenith", "eternity", "rhapsody", "wanderlust", "prosperity", "vibrant", "paradise", "serendipity",
    "breeze", "twilight", "mysterious", "whimsical", "velvet", "enchanted", "glistening", "lullaby",
    "whirlwind", "flourish", "melody", "enigma", "celestial", "eternity", "whisper", "sparkle", "blossom",
    "inspiration", "captivate", "shimmer", "glow", "luminous", "captivating", "intuition", "majestic",
    "resonate", "crystal", "inspire", "mesmerize", "adventure", "perfection", "paradise", "miracle",
    "fantasy", "charisma", "ecstasy", "serendipity", "wanderlust", "labyrinth", "phenomenal", "wonderment",
    "enthusiasm", "imagination", "whimsy", "fascination", "harmonious", "illuminated", "spellbound",
    "eclectic", "brilliance", "exploration", "magnificent", "unforgettable", "enigmatic", "euphoria",
    "tranquil", "radiant", "serenity", "elegant", "rhapsody", "adventure", "harmony", "dreamscape", "ethereal",
    "captivating", "effulgent", "paradox", "breathtaking", "enchanting", "mellifluous", "captivation",
    "fantasia", "enchant", "divine", "idyllic", "lighthearted", "splendor", "iridescent", "surreal",
    "astounding", "utopia", "infinite", "verdant", "luminescent", "harbor", "beauty", "liberty", "cheer",
    "brio", "carnival", "jovial", "lively", "rejoice", "melodic", "jubilation", "idyllic", "panorama",
    "tranquil", "prosperity", "bliss", "gala", "quixotic", "celestial", "imagination", "zephyr", "zenith",
    "seraphic", "tempest", "mystique", "jocund", "sonorous", "intrepid", "ebullient", "ethereal", "nostalgic",
    "gratitude", "charismatic", "scintillate", "luminosity", "effulgence", "epiphany", "pinnacle", "captivation",
    "reflection", "lighthearted", "marvel", "enigmatic", "quiescent", "serendipitous", "effervesce", "imagine",
    "mellifluous", "blissful", "resonate", "enthralling", "mystical", "tranquility", "eternity", "rhapsody",
    "perennial", "dreamscape", "harmonious", "labyrinth", "exuberance", "vivid", "inspiration", "wanderlust",
    "illustrious", "oasis", "synchronicity", "ecstasy", "mesmerize", "universe", "zephyr", "eclectic", "serenity",
    "serendipity", "luminous", "jubilation", "paradise", "whimsical", "breathtaking", "adventure", "celebration",
    "magnificent", "cascade", "lullaby", "effervescent", "captivate", "fantasy", "phenomenal", "majestic"]
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
    while True:
        play_again = input("/ Play again? (y/n): ").lower()
        if play_again == "y":
            hangman()
        elif play_again == "n":
            sys.exit(1)
        else:
            print("/ Please enter 'y' to play again or 'n' to exit.")
hangman()
