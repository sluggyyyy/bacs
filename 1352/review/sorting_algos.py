def bubble_sort(items):
    for i in range(len(items)):
        for j in range(len(items) - i - 1):
            if items[j] > items[j + 1]:
                items[j], items[j + 1] = items[j + 1], items[j]
    return items
        
def insertion_sort(items):
    for i in range(1, len(items)):
        while items[i - 1] > items[i] and i > 0:
            items[i], items[i - 1] = items[i - 1], items[i]
            i = i - 1
    return items