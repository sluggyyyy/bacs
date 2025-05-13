from hash_map import HashMap

anagrammap = HashMap()

with open("1353/labs/lab_12/Dictionary.txt", "r") as file:
    for line in file:
        word = line.strip()
        anagrammap.put_anagram(word)

anagrammap.print_anagrams("silent")