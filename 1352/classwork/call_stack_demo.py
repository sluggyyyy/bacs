def fourth(number: int) -> int:
    partial_result = cube(number)
    return partial_result * number

def cube(number: int) -> int:
    partial_result = square(number)
    return partial_result * number

def square(number: int) -> int:
    return number * number

def main():
    value = int(input("What integer do you want?\n"))
    print(f'\nThe fourth power of {value} is {fourth(value)}')
    
if __name__ == '__main__':
    main()