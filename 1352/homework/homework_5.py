from __future__ import annotations
class Fraction:
    def __init__(self, n = 1, d = 1):
        self.numerator = n
        self.denominator = d
    
    def __str__(self):
        return f'{self.numerator}/{self.denominator}'
    
    def __eq__(self, other: Fraction):
        return self.numerator * other.denominator == self.denominator * other.numerator
        
    def __lt__(self, other: Fraction):
        return self.numerator * other.denominator < self.denominator * other.numerator
    
    def __add__(self, other: Fraction):
        new_numerator = self.numerator * other.denominator + other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)
    
    def __mul__(self, other: Fraction):
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

my_fractions = [Fraction(1, i) for i in range(1, 101, 1)]


for f in my_fractions:
    print(f)






