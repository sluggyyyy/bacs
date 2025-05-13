it = iter(my_data)
while True:
    try:
        value = next(it)
    except StopIteration:
        break
    
# TypeError: List object is not iterable

# Create a new class to represent iterator objects 
# that will traverse your data

class Iterator: