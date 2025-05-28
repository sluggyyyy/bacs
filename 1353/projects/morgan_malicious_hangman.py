import random

#Load the dictionary from file and organize it by word length
def load_dictionary():
    word_list = {}
    with open('1353/projects/wordlist.10000.txt', 'r') as file:
        for line in file:
            word = line.strip().lower()
            if not word.isalpha():  #Skip words with punctuation or numbers
                continue
            word_length = len(word)
            if word_length not in word_list:
                word_list[word_length] = set()
            word_list[word_length].add(word)
    return word_list

#Prompt user to choose word length
def choose_word_length(word_dict) -> int:
    while True:
        word_length = input("Choose a word length: ")
        if word_length.isnumeric():
            wl = int(word_length)
            if wl in word_dict:
                return wl  #Return length only if we have words of that length
            else:
                print("No words of that length available.")
        else:
            print("Invalid input. Please enter a number.")
            
#Prompt user to choose number of incorrect guesses allowed
def num_guesses() -> int:
    while True:
        guesses = input("Choose number of allowed incorrect guesses: ")
        if guesses.isnumeric():
            return int(guesses)
        else:
            print("Invalid input. Please enter a number.")

#Cn hoose a random word (used for old honest hangman mode)
def choose_word() -> str:
    dictionary = load_dictionary()
    word = random.choice(dictionary[choose_word_length()])
    return word

#Group all words into families based on pattern
def get_largest_word_family(words, guess, current_display):
    families = {}

    for word in words:
        pattern = ""
        for i in range(len(word)):
            if word[i] == guess:
                pattern += guess
            else:
                pattern += current_display[i]  #Maintain revealed letters

        if pattern not in families:
            families[pattern] = set()
        families[pattern].add(word)

    #Select pattern with most words
    max_pattern = None
    max_words = set()

    for pattern in families:
        if len(families[pattern]) > len(max_words):
            max_pattern = pattern
            max_words = families[pattern]

    return max_pattern, max_words

#Play regular hangman once only one word is left
def hangman(word, remaining_guesses, guessed_letters, current_display):
    print("\nNormal Hangman begins. One word remains.")
    
    while "_" in current_display and remaining_guesses > 0:
        print(" ".join(current_display))  #Show current revealed letters

        guess = input("Guess a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("Invalid input. Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.add(guess)

        #Reveal all instances of correct gues
        if guess in word:
            for i in range(len(word)):
                if word[i] == guess:
                    current_display[i] = guess
        else:
            remaining_guesses -= 1  #Count as incorrect guess

    #Game outcome
    if "_" not in current_display:
        print("\nCongratulations! You guessed the word correctly!")
    else:
        print("\nGame over. You ran out of guesses.")

    print(f"The word was: {word}")
    play_again()
    return False

#Main malicious hangman logic. keeps the word hidden as long as possible
def malicious_hangman(possible_words, max_incorrect_guesses) -> bool:
    guessed_letters = set()
    print_answer = ["_"] * len(next(iter(possible_words)))  #Display state
    incorrect_guesses = 0
    
    print(f"Welcome to Malicious Hangman. You have {max_incorrect_guesses} guesses to get the word right.")
    
    while "_" in print_answer and incorrect_guesses < max_incorrect_guesses:
        print("\n" + " ".join(print_answer))
        print(f"Incorrect guesses: {incorrect_guesses}")
        
        guess = input("Guess a letter: ").lower()
        if not guess.isalpha() or len(guess) != 1:
            print("invalid input. Please enter a single letter.")
            continue
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue
        
        guessed_letters.add(guess)
        
        #Partition words into families based on guessed letter
        pattern, new_word_set = get_largest_word_family(possible_words, guess, print_answer)

        #If the pattern doesn't reveal anything new its an incorrect guess
        if pattern == "".join(print_answer):
            incorrect_guesses += 1
            print("Incorrect guess.")
        else:
            print_answer = list(pattern)

        possible_words = new_word_set

        #If only one word remains  switch to regular hangman mode
        if len(possible_words) == 1:
            print("Only one word left. You're now playing normal hangman!")
            return hangman(next(iter(possible_words)), max_incorrect_guesses - incorrect_guesses, guessed_letters, print_answer)
            
    #win/loss outcome
    if "_" not in print_answer:
        print("\nCongratulations! You guessed the word correctly!")
        print(f'The word was {"".join(print_answer)}!')
        return False
    else:
        print("\nGame over. You ran out of guesses.")
        print(f"The word was  {random.choice(list(possible_words))}")

#Ask if the player wants to play another round
def play_again() -> bool:
    choice = input("Would you like to play again? ")
    if choice.lower() == "yes":
        main()
    elif choice.lower() == "no":
        print("Thanks for playing!")
        return False
    else:
        print(f'Invalid input. Please enter "yes" or "no"')
        play_again()

#Start a new game
def main():
    dictionary = load_dictionary()

    while True:
        word_length = choose_word_length(dictionary)
        max_guesses = num_guesses()
        words = dictionary[word_length]  # All words of the chosen length
        malicious_hangman(words, max_guesses)

        # Ask to play again after the game ends
        if not play_again():
            break

            
if __name__ == "__main__":
    main()
