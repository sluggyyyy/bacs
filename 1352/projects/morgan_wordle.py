"""
    Description of program: Wordle-like guessing game
    Filename: morgan_wordle.py
    Author: Zachary Morgan  
    Date: 01/15/25
    Course: COMP1352
    Assignment: Project 2 - A word game
    Collaborators: N/A
    Internet Source: geeksforgeeks.org, stackoverflow.com
"""
import random

def get_five_letter_words()->list[str]:
    with open('morgan_word_dict.txt', 'r') as file:
        lines = [line.strip() for line in file]
        return lines
"""
    Reads lines from a text file, strips them of their newlines
    Parameters: N/A
    Return: Returns a list of strings derived from the lines in the .txt
"""

def check_correct(answer:str, guess:str)->bool:
    if answer.lower() == guess.lower():
        return True
    else: return False
"""
    Checks if the answer is equal to the guess
    Parameters: Takes in the answer, and the guess
    Return: Returns a boolean depending on whether the guess is correct or not
"""

def calculate_score(answer, guess:str)->str:
    guess = list(guess)
    answer = list(answer)
    colored_guess = [''] * len(guess)
    
    # Green Letters
    for letter in range(len(guess)):
        temp_answer = answer[:]
        if guess[letter] == temp_answer[letter]:
            colored_guess[letter] = green(guess[letter])
            temp_answer[letter] = '!'
            
    # Yellow Letters
    for letter in range(len(guess)):   
        if colored_guess[letter] == '':    
            if guess[letter] in temp_answer:
                colored_guess[letter] = yellow(guess[letter])
                temp_answer[temp_answer.index(guess[letter])] = '!'
                
    # Grey Letters
    for letter in range(len(guess)):
        if colored_guess[letter] == '':
            colored_guess[letter] = grey(guess[letter])
    return ''.join(colored_guess)
"""
    Generates a list from the guess string and answer string, initializes an empty list with 5 empty strings that is going to 
    hold the correctly colored guess letters as the function checks the letters in the guess against the ones in the answer.
    
    Begins by looping over the guess letters, creates a duplicate of the 'answer' list, if the current guess letter is equal to 
    the answer letter at the same index, turn the guess letter green and pop the answer letter off of its list by replacing it 
    with an '!'. 
    
    Second loop iterates over 'guess' again, checking if the letter in colored_ guess is already filled in in colored letter, if it is empty,
    check if the letter is inside of the answer list. If it is, change the value at 'letter' in colored_guess to a yellow version of
    guess[letter]. Replace the letter in temp_answer at index matching guess[letter] with an '!'
    
    Third loop iterates over 'guess' again, checking once again if the letter in colored_guess is empty or not, if it is empty at that index,
    fill it in with a grey version of guess[letter] because it has already been checked for yellow and green conditions
    
    Return colored_guess by joining it into a string with no spaces ('').
    
    Parameters: Takes in the answer and a guess
    Return: Returns a boolean depending on whether the guess is correct or not
"""

def yellow(s, end=''):
   return f'\u001b[43;1m{s.upper()}\033[0m'

def grey(s, end=''):
   return f'\u001b[47;1m{s.upper()}\033[0m'

def green(s, end=''):
   return f'\u001b[42;1m{s.upper()}\033[0m'
"""
    All three of these functions use unicode coloring to return a colored version of the string inputted
    Parameters: Takes in a string
    Return: Returns a colored version of string in parameters
"""    
                     
def generate_instructions():
    print(
        f"Welcome to {green('W')}{yellow('O')}{grey('R')}{green('D')}{yellow('L')}{grey('E')}!\n"
        "==================\n"
        "1. You have six attempts to guess a five-letter word.\n"
        "2. Each guess must be a valid five-letter word. Press Enter to submit.\n"
        "3. After each guess, the letters will change color to show how close your guess was to the word:\n"
        "   - Green: The letter is in the correct position.\n"
        "   - Yellow: The letter is in the word but in the wrong position.\n"
        "   - Gray: The letter is not in the word at all.\n"
        "Good luck and have fun!"
    )  
"""
    Prints out a list of instructions and a little welcome page with fancy colors :)
    Parameters: N/A
    Return: N/A
"""

def main() :
    # Generate the word list
    word_list = get_five_letter_words()
    # Pick a random choice from the word list to use as the answer
    answer = random.choice(word_list)
    # Initialize guess counter and set it to 0
    guess_count = 0
    # Initialize a list of previous guesses
    previous_guesses = []
    # Generate instructions and welcome page for user
    generate_instructions()
    # Begin game loop
    while True:
            # Ask user for input, store value as a string in 'guess'
            guess = input('\nMake a guess: ')
            # If the length of guess is 5 and the guess is letters, continue
            if len(guess) == 5 and guess.isalpha():
                # If the guess count is less than 5 and the guess is NOT the answer, continue
                # Check if the guess is == to the answer or not, if it is, continue
                if check_correct(answer, guess) == True:
                    # Let the user know they guessed the correct answer
                    print(f'You guessed it! {green(answer)}!\n') 
                    # Break out of while loop and kill program
                    break
                # If guess != answer, continue
                elif guess_count < 5:
                    # Check if the guess is in the word list
                    if guess.lower() in word_list:
                            # Loop over and print previous_guesses at the top of main conditional so user can see all previous feedback
                            # before their next guess
                            for previous_guess in previous_guesses:
                                print(previous_guess)
                            # Increment guess_count
                            guess_count += 1
                            # Initialize current_guess holding the calculated score of the users guess against the answer
                            current_guess = calculate_score(answer.lower(), guess.lower())
                            # Print the user's current guess
                            print(current_guess)
                            # Append the post-calculation current guess to previous guesses so that the user can see the colored version
                            # of their previous guess on the next loop
                            previous_guesses.append(current_guess)
                    else:
                        # If the lowercase version of the guess is not in the dictionary, output it in yellow and let user know
                        print(f'{yellow(guess.upper())} is not in our dictionary. ')
                else:
                    # If user has run out of guesses, let them know and show them correct answer
                    print(f'\nYou have run out of guesses!')
                    print(f'\nThe answer was {green(answer)}')
                    # Break out of while loop and kill program
                    break
            # If guess is longer than 5 letters or not alphabetical, let them know and do not count the guess against them
            else: print('Guesses must be five-letter words only.')

if __name__ == '__main__' :
    main()