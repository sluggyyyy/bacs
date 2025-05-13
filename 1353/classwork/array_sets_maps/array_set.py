import re
class ArraySet:

    def __init__(self):
        # store the contents of the set in a python list,
        # which is itself a (dynamic) array
        self.the_set = []

    def __iter__(self):
        # made so easy since the contents are stored in a python
        # list which is already iterable
        return iter(self.the_set)
    
    def __str__(self):
        result = "{"
        for x in self.the_set:
            result += str(x) + ", "
        return result.rstrip(", ") + "}"

    def get_size(self):
        return len(self.the_set)

    def add(self, v):
        # No duplicates allowed in sets, so make sure v is not
        # already in the set. If not, then add it (by appending
        # it to the end of the list)
        if not v in self.the_set:
            self.the_set.append(v)

    def discard(self, v):
        # this one was easy since python list already has
        # a remove method which removes the first found
        # occurrence of v. But the_set can have no duplicates
        # so this works!
        try:
            self.the_set.remove(v)
        except:
            return

    def contains(self, v)->bool:
        return v in self.the_set

    def union(self, other):
        union_set = ArraySet()
        for item in self.the_set:
            union_set.add(item)
        for item in other:
            union_set.add(item)
        return union_set

    def intersection(self, other):
        intersection_set = ArraySet()
        for item in self.the_set:
            if item in other:
                intersection_set.add(item)
        return intersection_set

    def difference(self, other):
        difference_set = ArraySet()
        for item in self.the_set:
            if item not in other:
                difference_set.add(item)
        return difference_set
  
def read_strings_from_file(file_path):
        with open(file_path, "r") as file:
            strings = file.readlines() 
            strings = [re.sub(r'\d+', '', s).strip() for s in strings]
        return strings
    
def main():
    male_names = ArraySet()
    female_names = ArraySet()
    

    males = read_strings_from_file("1353/classwork/array_sets_maps/maleNames2016.txt")
    females = read_strings_from_file("1353/classwork/array_sets_maps/femaleNames2016.txt")
    
    for name in males:
        male_names.add(name.strip().replace("\ufeff", ""))
    
    for name in females:
        female_names.add(name.strip().replace("\ufeff", ""))
    
    intersection_names = male_names.intersection(female_names)
    
    print(intersection_names)
    print(intersection_names.get_size())
    
if __name__ == "__main__":
    main()