from projects.morgan_pico_fermi_bagels import *

# Devin
"""
def test_count_matches():
   # No matches
   assert count_matches('123', '456') == (0, 0), "Expected (0, 0) for '123' vs. '456'"
   # One Fermi (correct digit in the correct place)
   assert count_matches('456', '412') == (1, 0), "Expected (1, 0) for '456' vs. '412'"
   # One Pico (correct digit in the wrong place)
   assert count_matches('789', '172') == (0, 1), "Expected (0, 1) for '789' vs. '172'"
   # Multiple Fermi and Pico
   assert count_matches('123', '132') == (1, 2), "Expected (1, 2) for '123' vs. '132'"


# detect_duplicates
#   consumes a three-symbol word and determines if there are any duplicate symbols
#   produces True if there are duplicate symbols and False otherwise
def test_detect_duplicates():
   assert detect_duplicates('111'), "'111' has duplicate digits and should return True"
   assert detect_duplicates('121'), "'121' has duplicate digits and should return True"
   assert not detect_duplicates('987'), "'987' has no duplicates and should return False"


# random_code
# produces a three-symbol word with no duplicates
def test_random_code():
   result = random_code()
   # Check if the result is the correct length
   assert len(result) == 3, f"Expected length 3 but got {len(result)}"
   # Check if each character appears only once
   assert not detect_duplicates(result), f"Expected no duplicates in {result}"
   # Check if all characters are digits
   assert result.isdigit(), f"Expected all digits in {result}"


# output_result
# consumes a tuple (f, p) where f is the number of Fermi and p is the number of Pico
# produces a string containing the word Fermi repeated f times and Pico repeated p times
def test_output_result():
   assert output_result((0, 0)) == 'Bagels!', "Expected 'Bagels!' for (0, 0)"
   assert output_result((1, 0)) == 'Fermi!', "Expected 'Fermi!' for (1, 0)"
   assert output_result((0, 1)) == 'Pico!', "Expected 'Pico!' for (0, 1)"
   assert output_result((1, 2)) == 'Fermi! Pico! Pico!', "Expected 'Fermi! Pico! Pico!' for (1, 2)"
   assert output_result((3, 0)) == 'Fermi! Fermi! Fermi!', "Expected 'Fermi! Fermi! Fermi!' for (3, 0)"
   assert output_result((0, 3)) == 'Pico! Pico! Pico!', "Expected 'Pico! Pico! Pico!' for (0, 3)"
"""

# Mya

def test_count_matches() :
   # example tests
   assert count_matches( '123', '456' ) == (0, 0)
   # 4 is in the correct place so one fermi is expected
   assert count_matches( '456', '412' ) == (1, 0)
   # 7 is in the answer but in the wrong location so one pico is expected
   assert count_matches( '789', '172' ) == (0, 1)
   # No matching digits, completely incorrect guess
   assert count_matches('123', '231') == (0, 3)
   # All digits match in the correct positions
   assert count_matches('123', '123') == (3, 0)
   # One digit matches in the correct position, two match in incorrect positions
   assert count_matches('345', '354') == (1, 2)
   # Additional cases
   assert count_matches('000', '123') == (0, 0)  # No matching digits
   assert count_matches('123', '000') == (0, 0)  # No matching digits
   assert count_matches('987', '789') == (1, 2)  # Mixed Fermi and Pico
   assert count_matches('123', '132') == (1, 2)  # One Fermi, two Picos
   assert count_matches('888', '888') == (3, 0)  # All Fermis (same repeated digit)
   assert count_matches('123', '312') == (0, 3)  # All Picos in different order
   # Test case to check for only numeric characters
   assert count_matches('123abc', '1a2b3c') == (1, 2)


def test_detect_duplicates():
   assert detect_duplicates( '123' ) == False, '123 has no duplicate symbols but detect_duplicates returned True'
   assert detect_duplicates( '111' ) == True, '111 has duplicate symbols but detect_duplicates returned False'
   assert detect_duplicates('112') == True
   assert detect_duplicates('1a1') == True
   assert detect_duplicates('abc') == False
   assert detect_duplicates('000') == True  # All zeros
   assert detect_duplicates('101') == True  # One duplicate
   assert detect_duplicates('120') == False  # No duplicates


def test_random_code():
  result = random_code()
  # Check if the result is the correct length
  assert len(result) == 3, f"Expected length 3 but got {len(result)}"
  # Check if all characters are digits
  assert result.isdigit(), f"Expected all digits in {result}"
  # Check if all characters are unique
  assert not detect_duplicates(result)


def test_output_result() :
   assert output_result((0, 0)) == 'Bagels!'
   assert output_result((1, 0) ) == 'Fermi!'
   assert output_result((0, 1)) == 'Pico!'  # One Pico
   assert output_result((0, 2)) == "Pico! Pico!"
   assert output_result((1, 1)) == "Fermi! Pico!"
   assert output_result((2, 1)) == 'Fermi! Fermi! Pico!'  # Two Fermis, one Pico
   assert output_result((1, 2) ) == 'Fermi! Pico! Pico!'
   assert output_result((0, 3)) == 'Pico! Pico! Pico!'  # Three Picos
   assert output_result((3, 0)) == "Fermi! Fermi! Fermi!"