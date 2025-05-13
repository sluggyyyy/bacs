# Add the integers from 1 to n
# Base Case: when n == 1, the sum is 1
# Recursive Relationship: sum of first n numbers is n + sum of first n - 1 numbers

def sum_of_first_n(n: int) -> int:
    if n == 1:
        return 1
    else:
        return n + sum_of_first_n(n - 1)
        
print(f'Sum of first 999 positive integers is {sum_of_first_n(999)}')