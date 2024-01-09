import random, os, time, sys
words = ["apple", "banana", "orange", "grape", "strawberry", "carrot", "broccoli", "potato", "pizza", "burger", "sandwich", "pasta", "rice", "chocolate", "coffee", "tea", "water", "juice", "bread", "cheese", "chicken", "beef", "fish", "salad", "ice cream", "cake", "cookie", "candy", "milk", "egg", "butter", "onion", "tomato", "pepper", "salt", "car", "truck", "bus", "motorcycle", "bicycle", "train", "airplane", "boat", "ship", "subway", "taxi", "van", "truck", "scooter", "helicopter", "motorboat", "sailboat", "tractor", "ambulance", "firetruck", "police car", "taxi", "suv", "minivan", "convertible", "limousine", "pickup truck", "sedan", "wagon", "aircraft", "spaceship", "rocket", "satellite", "spacesuit", "planet", "star", "moon", "sun", "galaxy", "universe", "astronaut", "spaceship", "comet", "asteroid", "meteor", "spacesuit", "earth", "vegetable", "fruit", "meat", "dairy", "beverage", "dessert", "snack", "transportation", "vehicle", "space", "celestial", "body", "nature", "animal", "fish", "bird", "mammal", "reptile", "amphibian", "insect", "plant", "flower", "tree", "forest", "mountain", "river", "ocean", "lake", "desert", "island", "beach", "sky", "cloud", "rain", "snow", "weather", "season", "spring", "summer", "fall", "autumn", "winter", "sunrise", "sunset", "cloudy", "windy", "storm", "rainbow", "star", "moonlight", "night", "day", "morning", "afternoon", "evening", "nighttime", "noon", "midnight", "rainbow", "cloudy", "sunny", "snowy", "foggy", "clear", "thunderstorm", "tornado", "quicksand", "avalanche", "quasar", "blackhole", "nebula", "supernova", "quark", "lepton", "proton", "neutron", "electron", "atom", "molecule", "cell", "organism", "living", "dead", "dry", "wet", "hot", "cold", "fast", "slow", "strong", "weak", "young", "old", "male", "female", "child", "adult", "elderly", "human", "alien", "extraterrestrial", "species", "genus", "family", "order", "class", "kingdom", "phylum", "domain", "eukaryota", "prokaryota", "archaea", "bacteria", "virus", "fungi", "moss", "fern", "conifer", "angiosperm", "monocot", "dicot", "herb", "shrub", "grass", "tree", "plant", "flower", "root", "leaf", "stem", "branch", "twig", "seed", "fruit", "nut", "berry", "bulb", "rhizome", "blossom", "petal", "stamen", "pistil", "pollen", "nectar", "nectary", "bud", "twig", "branch", "trunk", "wood", "bark", "foliage", "flora", "fauna", "ecosystem", "habitat", "biome", "continent", "country", "state", "province", "city", "town", "village", "hamlet", "island", "archipelago", "oasis", "desert", "jungle", "forest", "swamp", "marsh", "wetland", "coral", "reef", "ocean", "sea", "bay", "gulf", "strait", "sound", "lake", "pond", "pool", "river", "stream", "waterfall", "gorge", "valley", "mountain", "hill", "mesa", "plateau", "plain", "basin", "range", "chain", "group", "cluster", "volcano", "lava", "magma", "igneous", "sedimentary", "metamorphic", "igneous", "word", "language", "phrase", "sentence", "paragraph", "article", "book", "story", "novel", "poetry", "verse", "song", "music", "art", "painting", "sculpture", "drawing", "design", "architecture", "construction", "engineering", "mathematics", "physics", "chemistry", "biology", "geology", "history", "politics", "law", "religion", "spirituality", "ethics", "morality", "philosophy", "psychology", "sociology", "anthropology", "computer", "internet", "technology", "phone", "tablet", "keyboard", "mouse", "screen", "monitor", "software", "hardware", "program", "code", "data", "file", "folder", "email", "message", "chat", "website", "social media", "search", "browser", "server", "database", "network", "cybersecurity", "password", "username", "login", "logout", "download", "upload", "camera", "photo", "video", "audio", "music", "movie", "gaming", "console", "controller", "player", "team", "sport", "exercise", "health", "fitness", "nutrition", "sleep", "dream", "meditation", "mindfulness", "stress", "anxiety", "depression", "happiness", "joy", "laughter", "friendship", "family", "love", "relationship", "marriage", "divorce", "single", "dating", "parenting", "childhood", "adolescence", "adulthood", "senior", "retirement", "work", "job", "career", "employment", "business", "money", "finance", "economy", "market", "investment", "budget", "income", "expense", "savings", "debt", "credit", "shopping", "fashion", "style", "beauty", "hair", "makeup", "skincare", "body", "mind", "soul", "spirit", "consciousness", "awareness", "knowledge", "learning", "education", "school", "college", "university", "teacher", "student", "classroom", "lecture", "exam", "test", "grade", "degree", "diploma", "certificate", "research", "discovery", "innovation", "invention", "technology", "science", "scientist", "researcher", "experiment", "theory", "hypothesis", "analysis", "observation", "conclusion", "result", "fact", "fiction", "imagination", "creativity", "inspiration", "motivation", "ambition", "goal", "dream", "aspiration", "achievement", "success", "failure", "challenge", "obstacle", "opportunity", "growth", "improvement", "development", "progress", "change", "transformation", "evolution", "revolution", "history", "past", "present", "future", "time", "space", "dimension", "reality", "illusion", "perception", "consciousness", "mind", "body", "soul", "spirit", "energy", "vibration", "frequency", "matter", "particle", "wave", "quantum", "cosmos", "galaxy", "star", "planet", "earth", "nature", "universe", "infinity", "eternity", "existence", "creation", "divinity", "spirituality", "religion", "faith", "belief", "ritual", "ceremony", "worship", "prayer", "meditation", "enlightenment", "awakening", "truth", "wisdom", "knowledge", "understanding", "insight", "intuition", "awareness", "consciousness", "self", "identity", "ego", "mind", "body", "soul", "spirit", "essence"]
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
def choose_word():
    return random.choice(words)
def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter.isalpha() and letter in guessed_letters:
            display += letter
        elif letter.isspace():
            display += " "
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
