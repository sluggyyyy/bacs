import random

def load_dictionary():
    word_list = {}
    with open('1353/projects/wordlist.10000.txt', 'r') as file:
        words = [line.strip() for line in file]
        for word in words:
            word_length = len(word)
            if word_length not in word_list:
                word_list[word_length] = []
            word_list[word_length].append(word)
    return word_list 

def choose_word_length() -> int:
    while True:
        word_length = input("Choose a word length: ")
        
        if word_length.isnumeric():
            return int(word_length)
        else:
            print("Invalid input. Please enter a number.")
        

def choose_word() -> str:
    dictionary = load_dictionary()
    word = random.choice(dictionary[choose_word_length()])
    return word


def hangman(word) -> bool:
    word = word.lower()
    guessed_letters = set()
    print_answer = ["_"] * len(word)
    max_incorrect_guesses = 10
    incorrect_guesses = 0
    
    print(f"Welcome to Hangman. You have {max_incorrect_guesses} guesses to get the word right.")
    
    while print_answer != list(word):
        
        print("\n" + " ".join(print_answer))
        print(f"Incorrect guesses: {incorrect_guesses}")
        
        if incorrect_guesses >= max_incorrect_guesses:
            print("Game over. You ran out of guesses.")
            play_again()
            return False
        
        guess = input("Guess a letter: ")
        
        if not guess.isalpha() or len(guess) != 1:
            print("Invalid input. Please enter a single letter.")
            continue
        
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue
        
        guessed_letters.add(guess)
        
        if guess in word:
            for i in range(len(word)):
                if word[i] == guess:
                    print_answer[i] = guess
        else:
            incorrect_guesses += 1
            print("Incorrect guess.")
        
        if print_answer == list(word):
            print("\nCongratulations. You guessed the word correctly!")
            print(print_answer)
            return False
        
    return False

def play_again() -> bool:
    choice = input("Would you like to play again? ")
    if choice.lower() == "yes":
        word = choose_word()
        hangman(word)
    elif choice.lower() == "no":
        print("Thanks for playing!")
    else:
        print(f'Invalid input. Please enter "yes" or "no"')
        play_again()

def main():
    word = choose_word()
    while hangman(word) == True:
        hangman(word)
            
if __name__ == "__main__":
    main()