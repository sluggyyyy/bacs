# [1 1 1 1 1 1 1]
# [2, 4, 8, 16, 32, 64]

# my_list = []
# for i in range (1, 5):
#     temp_list = []
#     for j in range(1, 7):
#         temp_list.append(i ** j)
#     my_list.append(temp_list)
    
# my_list = [[i**j for j in range(1, 7)] for i in range(1, 5)]

# print(my_list)

# def factorial(n):
#     if n == 0:
#         return 1
#     elif n < 0:
#         return -1
#     else:
#         return n * factorial(n - 1)

# print(factorial(-2))  # should print -1
# print(factorial(0))   # should print 1
# print(factorial(0))   # should print 1
# print(factorial(5))   # should print 120

# class Complex:
#     def __init__(self, n1, n2):
#         self.number1 = n1
#         self.number2 = n2
        
#     def __str__(self):
#         return f'{self.number1} + {self.number2}i'
    
#     def __add__(self, other):
#         result1 = self.number1 + other.number1
#         result2 = self.number2 + other.number2
#         return Complex(result1, result2)
    
#     def __sub__(self, other):
#         result1 = self.number1 - other.number1
#         result2 = self.number2 - other.number2
#         return Complex(result1, result2)
    
#     def __eq__(self, other):
#         return self.number1 == other.number1 and self.number2 == other.number2



# def main():
#     c1 = Complex(5, -1)
#     c2 = Complex(2, 3)
#     c3 = Complex(7, 2)
#     print(f"{c1},  {c2}, {c3}") # outputs 5 + -1i,  2 + 3i, 7 + 2i
#     print(c1+c2)                # outputs 7 + 2i
#     print(c1-c2)                # outputs 3 + -4i
#     print(c1)                   # outputs 5 + -1i
#     print(c1 == c1)		# outputs True
#     print(c1 == c2)             # outputs False
#     print(c1 + c2 == c3)        # outputs True
    
# if __name__ == '__main__':
#     main()

# def print_pyramid(SIZE):
#     for row in range(SIZE):
#         print(" " * (SIZE - row - 1), end = '')
#         print("*" * (2*row-1), end='')
#         print()
    
# print_pyramid(5)

