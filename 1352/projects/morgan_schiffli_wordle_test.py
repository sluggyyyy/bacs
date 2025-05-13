from morgan_wordle import *
def test_get_five_letter_words() :
    # example tests
    word_list = get_five_letter_words()
    # verify all words are length five
    for word in word_list:
        assert len(word) == 5, f"Expected a five letter word, but got {word}"
    # verify that specific words are in the list
    assert 'apple' in word_list, "Expected 'apple' in the list of five letter words"
    assert 'zebra' in word_list, "Expected 'zebra' in the list of five letter words"
    assert 'until' in word_list, "Expected 'until' in the list of five letter words"
    assert 'trucks' not in word_list, "Expected 'trucks' not in the list of five letter words"
    assert 'zebras' not in word_list, "Expected 'zebras' not in the list of five letter words"

def test_calculate_score() :
    # arrow should not match until in any way
    assert calculate_score( 'until', 'arrow' ) == f"{grey('A')}{grey('R')}{grey('R')}{grey('O')}{grey('W')}", f"For goal word 'until', the guess 'arrow' should result in 'BBBBB'. Your result was {calculate_score('until', 'arrow')}"
    # Check if a single character is matched and in right position
    assert calculate_score( 'apple', 'arrow' ) == f"{green('A')}{grey('R')}{grey('R')}{grey('O')}{grey('W')}", f"For goal word 'apple', the guess 'arrow' should result in 'GBBBB'. Your result was {calculate_score('apple','arrow')}"
    # Check if all characters can be matched
    assert calculate_score( 'until', 'until' ) == f"{green('U')}{green('N')}{green('T')}{green('I')}{green('L')}", f"For goal word 'until', the guess 'until' should result in 'GGGGG'. Your result was {calculate_score('until','until')}"
    # Check if a character is matched in the wrong position
    assert calculate_score( 'apple', 'until' ) == f"{grey('U')}{grey('N')}{grey('T')}{grey('I')}{yellow('L')}", f"For goal word 'apple', the guess 'until' should result in 'BBBBY'. Your result was {calculate_score('apple','until')}"
    # Check if all characters matched in the wrong position
    assert calculate_score( 'races', 'scare' ) == f"{yellow('S')}{yellow('C')}{yellow('A')}{yellow('R')}{yellow('E')}", f"For goal word 'races', the guess 'scare' should result in 'YYYYY'. Your result was {calculate_score('races','scare')}"