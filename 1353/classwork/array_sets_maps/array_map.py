class Item:
    def __init__(self, k, v):
        self.key = k
        self.value = v
    
    def __str__(self):
        return f'{self.key}:{self.value}'
    
class ArrayMap:
    def __init__(self):
        self.the_map = []
    
    def get_size(self):
        return len(self.the_map)
    
    def is_empty(self):
        return len(self.the_map) == 0
    
    def get(self, k):
        for item in self.the_map:
            if item.key == k:
                return item.value
    
    def put(self, k, v):
        for item in self.the_map:
            if item.key == k:
                old_value = item.value
                item.value = v
                return old_value
        new_item = Item(k, v)
        self.the_map.append(new_item)
        return None
    
    def remove(self, k):
        for i in range(len(self.the_map)):
            if self.the_map[i].key == k:
                return_value = self.the_map[i].value
                self.the_map[i] = self.the_map[-1]
                del self.table[-1]
                return return_value
            else:
                return None
                
                
    
    def keys(self):
        pass