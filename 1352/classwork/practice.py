
# Assume that n is greater than or equal to 1
def mystery(n):
    if(n == 1):
        return 0
    else:
        return 1 + mystery(n//2)

print(mystery(1))
print(mystery(5))
print(mystery(17))