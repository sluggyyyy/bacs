import random

def check_sorted(int_list: list) -> bool:
    return all(int_list[i] <= int_list[i + 1] for i in range(len(int_list) - 1))



random.seed( 2013 )
for n in range( 6 ) :
    a_list = [ random.randint(count, count+3) for count in range(10) ]
    print( f"list: {n}: {a_list} check_sorted produced: {check_sorted(a_list)}")

