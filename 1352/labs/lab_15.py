
import numpy as np
# this array can hold up to 100 numbers
# Do not change the code below.
np.random.seed(13)
numbers = np.zeros(100, dtype = int)
for i in range(20):
    # generate a single random integer, loading one at a time into the array
    numbers[i] = np.random.randint(1, 100)
print(numbers)
# Notice that the array has a capacity 100, but contains only 20 random values
# Now insert a 0 at the start of the array. Notice that to do so you
# will have to first shift the 20 random values down one position in the array
# Output the contents of the array when you are done.
numbers[1:21] = numbers[0:20]

# Insert 0 at the start of the array
numbers[0] = 0

# Output the modified array
print("The array with the 0 inserted is:", numbers)