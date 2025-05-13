    ### Part 1
# def sum_of_squares(n: int) -> int:
#     answer = 0
#     if n < 0:
#         return -1
#     else:
#         for i in range(1, n + 1):
#             answer += (i**2)
#         return answer

# def main():
#     num = int(input("This program will find the sum of the first n squares. Enter n: "))
#     print(f'The sum of the first {num} squares is {sum_of_squares(num)}') 

# if __name__ == "__main__":
#     main()

# def test_sum_of_squares():
#     test_list = [(-100, -1), (-1, -1), (0,0), (1,1), (2, 5), (3, 14), (7, 140), (10, 385), (100, 338350), (500, 41791750)]
#     for pair in test_list:
#         assert sum_of_squares(pair[0]) == pair[1], f"Sum of first {0} squares should be {pair[1]}, not {sum_of_squares(pair[0])}"
#     print("All tests passed")
    
# test_sum_of_squares()

    ### Part 2
# def rec_sum_of_squares(n: int) -> int:
#     if n == 1:
#         return 1
#     elif n < 0:
#         return -1
#     else:
#         return n**2 + rec_sum_of_squares(n - 1)
    
# print(rec_sum_of_squares(999))
    
    ### Part 3
# def fibonacci(n: int) -> int:
#     times = 0
#     if n < 0:
#         return -1
#     if n == 1:
#         return 1
#     if n == 0:
#         return 0
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)

# def main():
#     index = int(input("Enter the index: "))
#     print(f'fibonacci({index}) is {fibonacci(index)}')
    
# if __name__ == "__main__":
#     main()

# def test_fibonacci():
#     test_list = [(-1, -1), (-10, -1), (0,0), (1,1), (2, 1), (3, 2), (4, 3), (5, 5), (6, 8), (7, 13), (10, 55)]
#     for pair in test_list:
#         assert fibonacci(pair[0]) == pair[1], f"fibonacci({pair[0]}) should return {pair[1]}, not {fibonacci(pair[0])}"

    ### Part 4
# def string_to_ord(s:str) -> list[int]:
#     result = []
#     for char in s:
#         result.append(ord(char))
#     return result

# def main():
#     the_string = input("This program will produce a list of ascii values from a string. Enter a string: ")
#     print(f'The ascii values of {the_string} are {string_to_ord(the_string)}')   

# if __name__ == "__main__":
#     main()

# def test_string_to_ord(): 
#     test_list = [("Alice",[65,108,105,99,101]),("Marya",[77,97,114,121,97]), ("Santiago",[83,97,110,116,105,97,103,111])] 
#     for pair in test_list: 
#         assert string_to_ord(pair[0]) == pair[1], f"Ascii values should be {pair[1]}, not {string_to_ord(pair[0])}" 
#     print("All tests passed")

    ### Part 5
# TODO: Write recursive rec_string_to_ord( s:str ) -> list[int] function
def rec_string_to_ord(s: str) -> list[int]:
    if s == "":
        return []
    else:
        return [ord(s[0])] + rec_string_to_ord(s[1:])

def main():
    the_string = input("This program will produce a list of ascii values from a string. Enter a string: ")
    print(f'The ascii values of {the_string} are {rec_string_to_ord(the_string)}')   

if __name__ == "__main__":
    main()

def test_rec_string_to_ord(): 
    test_list = [("Alice",[65,108,105,99,101]),("Marya",[77,97,114,121,97]), ("Santiago",[83,97,110,116,105,97,103,111])] 
    for pair in test_list: 
        assert rec_string_to_ord(pair[0]) == pair[1], f"Ascii values should be {pair[1]}, not {rec_string_to_ord(pair[0])}" 
        print("All tests passed")

