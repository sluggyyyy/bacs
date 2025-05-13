# cities = ["Denver", "Colorado Springs", "Pueblo"]

# content-based iteration
# for city in cities:
#     print(f'I love {city}!')
    
# index-based iteration
# for i in range(len(cities)):
#     if i < len(cities) - 1: 
#         print(f'I love {cities[i]}, ', end='')
#     else:
#         print(f'I also love {cities[i]}!')

# traversing using enumerate(), keep track of index and value simultaneously
# for i, city in enumerate(cities):
#     if i < len(cities) - 1:
#         print(f'I love {city}, ', end='')
#     else:
#         print(f'I also love {city}!')

# more_cities = [
#     ['Denver', 'Colorado Springs', 'Pueblo'],
#     ['Los Angeles', 'San Diego', 'Fresno'],
#     ['Chicago', 'Springfield', 'Champaign']
# ]

# content based iteration
# for row in more_cities:
#     for city in row:
#         print(f'I love {city}!')
        
# index based iteration
# for row_index in range(len(more_cities)):
#     for col_index in range(len(more_cities[row_index])):
#         print(f'I love {more_cities[row_index][col_index]}!')

# enumerate
# for row_index, row in enumerate(more_cities):
#     for col_index, city in enumerate(row):
        
# #Exercise: get all cities from one state onto one line

practice_list = [[507, 684, 67, 704, 959, 713, 907, 188, 909, 979, 989, 555, 145, 720, 874, 967, 365, 305, 685, 689, 157, 962, 137, 636, 748, 920, 354, 502, 521, 355], [254, 318, 651, 325, 343, 409, 875, 356, 38, 859, 864, 716, 938, 57, 820, 837, 441, 232, 56, 325, 434, 309, 167, 46, 469, 500, 648, 142, 604, 183], [533, 190, 195, 463, 784, 768, 45, 994, 516, 837, 640, 459, 705, 381, 617, 426, 558, 438, 460, 713, 734, 633, 353, 553, 287, 696, 176, 465, 4, 2], [175, 508, 827, 881, 854, 733, 969, 383, 514, 622, 95, 528, 199, 44, 728, 337, 185, 891, 968, 573, 676, 208, 320, 191, 773, 387, 115, 956, 395], [157, 340, 70, 889, 315, 114, 174, 319, 850, 819, 482, 767, 215, 776, 229, 651, 233, 225, 767, 633, 518, 630, 130, 608, 640, 723, 590, 533, 460, 999], [642, 382, 680, 353, 140, 399, 106, 938, 837, 22, 172, 889, 468, 190, 557, 47, 493, 278, 396, 62, 319, 6, 441, 9, 40, 152, 537, 354, 897, 674], [134, 469, 867, 979, 938, 641, 297, 455, 504, 89, 739, 907, 232, 324, 275, 296, 242, 882, 306, 363, 881, 865, 658, 616, 249, 567, 838, 59, 228, 157], [947, 633, 166, 101, 144, 166, 598, 537, 909, 617, 120, 26, 962, 792, 380, 756, 80, 377, 298, 699, 939, 406, 894, 108, 893, 851, 171, 182, 252, 542], [697, 402, 516, 166, 759, 842, 542, 756, 211, 21, 50, 115, 464, 290, 779, 805, 750, 808, 507, 77, 459, 617, 540, 997, 122, 762, 567, 516, 110, 123], [480, 541, 784, 262, 50, 651, 505, 890, 590, 838, 147, 672, 479, 772, 517, 152, 112, 802, 910, 588, 433, 677, 559, 587, 892, 483, 821, 947, 715, 397]]
print(len(practice_list))

for row in range(len(practice_list)):
    print(len(practice_list[row]))

print(f"Value at row index 3 column index 15 is {practice_list[3][15]}")

max = practice_list[0][0]
for row_index, row in enumerate(practice_list):
    for col_index, value in enumerate(row):
        if value > max:
            max = value
print(max)

for row_index, row in enumerate(practice_list):
    for col_index, value in enumerate(row):
        if value == 893:
            print(f'893 appears at row {row_index} and column {col_index}')
        

        
# write code to answer each of these questions:
# How many rows are there?
# Is the list jagged or rectangular?
# What value is stored at row index 3, column index 15?
# What is the maximum value stored in the list?
# Does the value 893 appear in the list? If so, what row/column? 