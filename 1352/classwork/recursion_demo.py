# # Calculate n! iteratively
# # def factorial(n: int)-> int:
# #     if n < 0:
# #         return -1
# #     answer = 1
# #     for i in range(2, n + 1):
# #         answer *= i
# #     return answer

# Calculate n! recursively
def factorial(n: int) -> int:
    if n == 0:
        return 1
    elif n < 0:
        return -1
    else:
        return n * factorial(n - 1)

def main():
    number = int(input('Enter the number you want the factorial of: '))
    print(f'{number} is {factorial(number)}')
    
if __name__ == '__main__':
    main()
