from random import randint, random, choice
import numpy as np
from dll import DoublyLinkedList
from collections import Counter

class Item:
    def __init__(self,k,v):
        self.key = k
        self.value = v
    def __str__(self):
        return f"{self.key}: {self.value}"
    def __repr__(self):
        return str(self)
    def set_value(self,new_value):
        old_value = self.value
        self.value = new_value
        return old_value
    
class HashMap:
    PRIMES = (393211,786433,1572869,3145739,6291479,12582969)
    
    def __init__(self):
        self._init_table(1000000)
    
    def _init_table(self, new_capcaity):
        self.the_table = np.empty(new_capcaity, dtype=DoublyLinkedList)
        self.prime = choice(HashMap.PRIMES)
        #a cannot be 0 becuase you cannot multiply by 0 since everything will end up in the same bucket
        self.a = randint(1, self.prime - 1)
        self.b = randint(0,self.prime-1)
        self.size = 0
        #Create buckets
        for i in range(len(self.the_table)):
            self.the_table[i] = DoublyLinkedList()
    
    def _hash_and_compress(self,k):
        #Hash function -> gives index
        return (hash(k) * self.a + self.b) % self.prime % len(self.the_table)

    def find_largest_anagram_group(hash_map):
        max_anagrams = 0
        largest_anagram_word = None

        # Loop through all buckets
        for bucket in hash_map.the_table:
            if bucket.size > max_anagrams:
                max_anagrams = bucket.size
                # The first element in the bucket represents the word
                largest_anagram_word = bucket.header.next.data.value if bucket.header.next.data else None
        
        return largest_anagram_word, max_anagrams
    
    def _string_hash(self, key):
        key = key.upper()
        counter = Counter(key)
        # Create a sorted tuple of (character, count) to guarantee order
        sorted_counter = tuple(sorted(counter.items()))
        return hash(sorted_counter) % len(self.the_table)
    
    def put_anagram(self, word):
        index = self._string_hash(word)
        bucket = self.the_table[index]
        for node in bucket:
            if node.value == word:
                return
        new_item = Item(word, word)
        bucket.add_first(new_item)
        self.size += 1
        if (self.size/len(self.the_table)) > 0.75:
            self._expand_table()
        return None
    
    def print_anagrams(self, word):
        index = self._string_hash(word)
        bucket = self.the_table[index]
        for node in bucket:
            print(node.value)
            
    def _expand_table(self):
        #store items in the table
        old_table = self.items()
        old_capacity = len(self.the_table)
        #Intianlize table with twice the number
        self._init_table(old_capacity * 2)
        for item in old_table:
             self.put_anagram(item.value)
    
    def get(self,k):
        #get the index of the bucket where key could exist
        index = self._hash_and_compress(k) #O(1)
        #get the bucket (DLL)
        bucket = self.the_table[index] #O(1)
        #iterate over the keys and return value if key is found
        for node in bucket:
            if node.value.key == k:
                return node.value.value
        return None
    
    def put(self,k,v):
        index = self._hash_and_compress(k)
        bucket = self.the_table[index]
        #Iterate over the kys
        for node in bucket:
            #IF we find the key
            if node.value.key == k:
                #Replace the old value with the new and return the old value
                node.value.value = v
                return
        new_item = Item(k,v)
        bucket.add_first(new_item)
        self.size += 1
        #TODO: Check if we need to expand the table here
        if (self.size/len(self.the_table)) > 0.75:
            self._expand_table()
        return None
    
    def remove(self,k):
        index = self._hash_and_compress(k)
        bucket = self.the_table[index]
        for node in bucket:
            if node.value.key == k:
                bucket.remove_between(node.prev.value, node.next.value)
                self.size -= 1
                return
    #Iterable Methods
    def keys(self):
        #Create an iterable
        the_keys = []
        #Iterate over the buckets
        for bucket in self.the_table:
            #iterate over the items
            for item in bucket:
                #Append the key to iterable
                the_keys.append(item.key)
        return the_keys
    
    def values(self):
        return[item.value for bucket in self.the_table for item in bucket]
    
    def items(self):
        return[item for bucket in self.the_table for item in bucket]
    
    def get_size(self):
        return self.size
    
    def is_empty(self):
        return self.size == 0
    
    #Make HashMap Iterable
    def __iter__(self):
        return iter(self.keys())
    
    def __str__(self):
        #Printing the items (iterable)
        return str(self.items())
    
    def output_table_info(self):
        max_bucket_size = 0
        #Print all the buckets
        for bucket in self.the_table:
            if bucket.size != 0:
                print(f"{bucket}")
        print("Size of largets bucket: ", max_bucket_size)
        print("Table size: ", self.size)
        print("Load Factor: ", self.size/len(self.the_table))