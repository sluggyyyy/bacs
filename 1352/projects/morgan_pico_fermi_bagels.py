"""
    Description of program: Guessing game that takes user input and compares it against a random fully unique 3 digit code
    Filename: morgan_pico_fermi_bagels.py
    Author: Zachary Morgan  
    Date: 01/10/25
    Course: COMP1352
    Assignment: Project 1 - A Guessing Game (called Pico Fermi Bagels)
    Collaborators: N/A
    Internet Source: geeksforgeeks.org, w3schools.com, stackoverflow.com
"""

import random

def count_matches(guess:str, answer:str)->tuple[int,int]:
    fermi = 0
    pico = 0
    remaining = list(answer)
    
    for i in range(len(guess)):
        if guess[i] == answer[i]:
            fermi += 1
            remaining[i] = None
            
    for i in range(len(guess)):
        if guess[i] != answer[i] and guess[i] in remaining:
            pico += 1
            remaining[remaining.index(guess[i])] = None
            
    return fermi, pico
"""
    Using parameters 'guess' and 'answer', open the function by creating three variables: 'fermi':int, 'pico':int and 'remaining':list
    containing the characters in 'answer'. Iterate for the length of 'guess' and see if any of the indexes match up exactly, if they do, 
    increment fermi. Iterate again over the length of 'guess', if the indexes do not match up exactly, but there are shared values in both, 
    increment pico. Both for loops end by replacing the matching (partially or exactly) index with None.
    parameters: guess string (user input) and answer string (random_code value)
    return: returns a tuple containing the values of fermi, and pico
"""
    
def detect_duplicates(guess:str)->bool:
    if guess.isnumeric():
        for char in guess:
            if guess.count(char) > 1:
                return True
            else:
                return False
    else:
        return None
"""
    Detect duplicates in player input using .count() method to count overlapping digits in the string.
    Parameters: Takes a string (from input())
    Return: Returns a boolean indicating whether duplicates are detected
"""
    
def random_code()->str:
    while True:
        number = random.randint(100, 999)
        number_str = str(number)
        
        if len(set(number_str)) == 3:
            return number_str
"""
    Generates a random 3 digit code and converts it to a string, checks if their are duplicates in the string by typecasting to a set
    (sets only hold unique values). If the length of the set is less than 3 digits, continue loop until the length is equal to three digits
    Parameters: No parameters are passed
    Return: Returns a string that contains the 3 digit code of unique characters
"""
def output_result(matches:tuple[int,int]) -> str:
    fermi, pico = matches
    if fermi or pico:
        return ' '.join(['Fermi!'] * fermi + ['Pico!'] * pico)
    else:
        return 'Bagels!'
"""
    This function outputs the proper amount of Fermi or Pico based off of a tuple parameter (fed by output of count_matches)
    parameters: Tuple input from count_matches that represent the number of Fermi (matches[0]) or Pico (matches[1])
    return: Returns a string of concatenated Fermi's and Pico's
"""
    
def generate_instructions():
    print('\nWelcome to Pico Fermi Bagels!')
    print('You will be given a 3-digit code to guess.')
    print('Your guess should contain only unique digits, guesses with repeat digits will count against you')
    print('Good luck!')
    print("To quit the game, type 'quit'.")
"""
    Generates instructions for player at the beginning of main() while loop
    parameters: N/A
    return: N/A
"""

def repeat_guess(input:str, previous_inputs:list) -> bool:
    if input in previous_inputs:
        return True
    else:
        return False
"""
    Checks user input against a list of previous inputs
    parameters: User input string and list of previous inputs
    return: Returns true if the user input is found in the list of previous inputs
"""
def main():
    # Generate instructions and the random number for the user to guess
    generate_instructions()
    answer = random_code()
    # Initialize list for 'previous_guesses' and the guess counter 'guesses'
    previous_guesses = []
    guesses = 0
    # Start a loop to play the game until the user quits or guesses correct answer
    while True:
        # Ask the user for a guess
        guess = input('\nPlease enter your guess: ')
        # Give feedback until the guess is correct (partially or fully)
        # If the user types quit break out of the while loop and end the program
        if guess.lower() == 'quit':
            break
        # If the string guess is not numeric or the length is less than 3, give the user negative feedback
        elif guess.isnumeric() == False or len(guess) != 3:
            print('Invalid guess. Guesses must be all digits with no repeats ')
        # If the string has duplicate digits give user negative feedback and count the guess against them
        elif detect_duplicates(guess):
            print ('Invalid guess. Guesses must be all digits with no repeats ')
            guesses += 1
        # Check if the user has already guessed their newest guess, if they have let them know. 
        # Do not count this guess against user
        elif repeat_guess(guess, previous_guesses):
            print('You already guessed that!')
        else:
        # Initialize matches variable taking in the guess and the answer strings
        # Output a tuple with the number of exact guesses and partial guesses respectively
            matches = count_matches(guess, answer)
        # Print the correct number of Fermi's and Pico's using the tuple 'matches' as input
            print(output_result(matches))
        # Add 1 guess to the guess counter
            guesses += 1
        # Add most recent guess to the list of previous guesses
        previous_guesses.append(guess)
        # If the user's guess is equal to the random code, let them know they correctly guessed
        # and how many guesses it took them. Break out of while loop and end program
        if guess == answer:
            print(f'\nYou got it in {guesses} guesses!')
            break
    
if __name__ == "__main__":
    main()