# This is a Binary <--> Decimal converter
# The Binary will be a list of integers representing the number

# Binary to Decimal
def binToDecList(bin):
    size = len(bin)
    dec = 0
    for pos in range(size):
       
        curDigit = bin[size-pos-1]      
        curPow = 2**pos

        dec += (curDigit * curPow)

    return dec




# Decimal to Binary
def decToBinList(d):
    bin = []

    numDigits = 0
    while 2**numDigits <= d:
        numDigits += 1
 
    for pos in range(numDigits-1, -1, -1):  # numDigits-1 down to and including 0
        curPow = 2**pos
  
        if d>=curPow:
            bin.append(1)
            d -= curPow
      
        else:
            bin.append(0)
       
    return bin

# Testing
print(binToDecList([1, 1, 0, 0, 1]))
print(decToBinList(25))

