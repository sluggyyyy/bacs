"""
    Description of program: Test file for morgan_pico_fermi_bagels.py
    Filename: morgan_test_pico_fermi_bagels.py
    Author: Zachary Morgan
    Date: 01/10/25
    Course: COMP1352
    Assignment: Project 1
    Collaborators:
    Internet Source: docs.pytest.org, Canvas documentation provided by professor
"""
from projects.morgan_pico_fermi_bagels import *
def test_count_matches() :
    assert count_matches( '123', '456' ) == (0, 0)
    assert count_matches( '456', '412' ) == (1, 0)
    assert count_matches( '789', '172' ) == (0, 1)
    assert count_matches( 'sky', '104' ) == (0, 0), 'User entered words instead of digits, count_matches produceed something other than 0,0'
    assert count_matches( '$$$', '194' ) == (0, 0), 'User entered symbols instead of digits, count_matches produced something other than 0,0'

def test_detect_duplicates() :
    assert detect_duplicates( '123' ) == False, '123 has no duplicate symbols but detect_duplicates returned True'
    assert detect_duplicates( '111' ) == True, '111 has duplicate symbols but detect_duplicates returned False'
    assert detect_duplicates( 'sky' ) == None, 'User entered words, detect_duplicates returned something other than None'
    assert detect_duplicates( '$$$' ) == None, 'User entered symbols, detect_duplicates returned something other than None'
    
def test_random_code() :
    result = random_code()
    assert len(result) == 3
    assert len(set(result)) == 3
    assert result.isnumeric() == True

def test_output_result() :
    assert output_result( (0, 0) ) == 'Bagels!'
    assert output_result( (1, 0) ) == 'Fermi!'
    assert output_result( (0, 1) ) == 'Pico!'
    assert output_result( (1, 2) ) == 'Fermi! Pico! Pico!'
    assert output_result( (2, 1) ) == 'Fermi! Fermi! Pico!'
    assert output_result( (1, 1) ) == 'Fermi! Pico!'
    
def test_repeat_guess() :
    assert repeat_guess('123', ['123', '456', '234']) == True, 'Expected True, received False'
    assert repeat_guess('123', ['789', '406', '145']) == False, 'Expected False, received True'