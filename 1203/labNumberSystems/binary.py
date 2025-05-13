# This is a Binary <--> Decimal converter

# Note that you are not allowed to use int(), str(), or bin() for this lab as that
#   is the behavior we are trying to implement

import math  # for log, floor

# Binary to Decimal
# Takes in a list of integers representing the binary number
#   If the binary number is 110, bin will be passed in as [1,1,0]
#     and the decimal result will be 6
def binToDecList(bin):
    size = len(bin)
    dec = 0

    for pos in range(size):
        curDigit = bin[size - pos - 1]
        curPow = 2**(pos)
        dec += (curDigit * curPow)

    return dec


# Decimal to Binary
# Takes in a decimal number, such as 6
# The result is a list of integers representing the binary number
# There are to be no leading zeros in the list
#  That is, if the input decimal is 6, then binary should be 110
#    and it should return [1,1,0]
def decToBinList(d):
    bin = []
    numDigits = math.floor(math.log(d, 2)) + 1
    
    for pos in range(numDigits, -1, -1):
        curPow = 2**pos
  
        if d>=curPow:
            bin.append(1)
            d -= curPow
            
        else:
            bin.append(0)
       
    return bin

def charToHex(c):
    return ord(c) - ord('A') + 10

def hexToChar(h):
    return chr(ord('A') + h - 10)

def decToBase(baseNum, base):
  digits = []
  num = baseNum

  while num > 0:
    remainder = num % base
    digits.insert(0, remainder)
    num //= base

  result = ""
  for digit in digits:
    if digit < 10:
      result += chr(digit + ord('0'))
    else:
      result += hexToChar(digit)

  return result

print(decToBase(25, 2))  # returns "11001"
print(decToBase(243, 16)) # returns "F3"

def baseToDec(dec: str, base: int):
  result = 0
  power = 0
  for char in reversed(dec):
    if '0' <= char <= '9':
      digit = ord(char) - ord('0')
    else:
      digit = charToHex(char.upper())
    result += digit * (base ** power)
    power += 1
  return result

print(baseToDec("11001", 2)) # returns 25
print(baseToDec("F3", 16)) # returns 243
print(baseToDec("f3", 16)) # returns 243