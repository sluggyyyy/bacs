# import random

# randos = []
# for i in range(10):
#     inner_list = []
#     for j in range(20):
#         inner_list.append(random.randint(0,9))
#     randos.append(inner_list)
        
# print(randos)

import random
import dudraw

random.seed(10011924)
num_rows = 5
num_cols = 8
nums = [[random.randint(0,100) for _ in range(num_cols)] for _ in range(num_rows)]
print(nums)

# total_sum = 0
# for row in nums:
#     for col in row:
#         total_sum += col
# print(total_sum)

# total_sum = 0
# for row in range(len(nums)):
#     for col in range(len(nums[row])):
#         total_sum += nums[row][col]
# print(total_sum)

# for row in nums:
#     total_row = 0
#     num_of_col = 0
#     for col in row:
#         print(f'{col} ', end='')
#         total_row += col
#         num_of_col += 1
#     print(f'| {total_row/num_of_col}')
#     print('\n')
  

# for row in nums:
#     lt_50 = 0
#     for col in row:
#         if col < 50:
#             lt_50 += 1
#     print(lt_50)

# for row in range(4):
#     for col in range(7):
#         print(row + col, end=' ')
#     print('\n')

for row in range(5):
    for col in range(5 - row):
        print(row, end = " ")
    print()
        