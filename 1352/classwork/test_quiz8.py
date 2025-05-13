def print_triangle(n: int):
    if n == 1:
        print('*')
    else:
        print_triangle(n - 1)
    print(n * '*', end = '')
    
print_triangle(5)