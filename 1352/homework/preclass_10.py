
def foo(some_list: list[int])->None:
    del some_list[0]

a = [6, 12, 15, 13]
b  = a
c = [6, 12, 15, 13]
b.pop() #removes and returns the last element in the list
c.append(20) 
foo(b)
foo(c)



print(a)

print(b)

print(c)


