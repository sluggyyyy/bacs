import pytest
from projects.morgan_wordle import check_correct, calculate_score, yellow, grey, green

# Mock data for testing

def test_check_correct():
    assert check_correct("apple", "apple") is True
    assert check_correct("Apple", "apple") is True
    assert check_correct("apple", "grape") is False

def test_calculate_score_green():
    result = calculate_score("apple", "apple")
    assert result == f"{green('A')}{green('P')}{green('P')}{green('L')}{green('E')}", f'Returned {result}'

def test_calculate_score_yellow_and_grey():
    result = calculate_score("apple", "grape")
    assert result == f"{grey('G')}{grey('R')}{yellow('A')}{yellow('P')}{green('E')}" , f'Returned {result}'

def test_yellow():
    assert yellow("a") == f'\u001b[43;1mA\033[0m'

def test_grey():
    assert grey("a") == f'\u001b[47;1mA\033[0m'

def test_green():
    assert green("a") == f'\u001b[42;1mA\033[0m'