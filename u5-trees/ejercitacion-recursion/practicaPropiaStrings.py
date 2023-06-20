# ATM Analogie

from operator import truediv
from types import NoneType


class Person:
    nextInLine = None

gustavo = Person()
patri = Person()
marcos = Person()
ana = Person()
augusto = Person()

augusto.nextInLine = ana
ana.nextInLine = marcos
marcos.nextInLine = patri
patri.nextInLine = gustavo

def getMyPositionInLine(person):
    if (person.nextInLine == None):
        return 1
    
    return 1 + getMyPositionInLine(person.nextInLine)

# print(getMyPositionInLine(augusto))

# String reverse

# using recursion
def stringReverse(input):
    if len(input) == 0:
        return input
    return stringReverse(input[1:]) + input[0]

myString = 'Hola'

stringReversed = stringReverse(myString)

#print(stringReversed)

# using stack

def newStack():
    stack = []
    return stack

def isEmpty(stack):
    if len(stack) == 0:
        return True

def push(stack,element):
    stack.append(element)

def pop(stack):
    if isEmpty(stack):
        return
    return stack.pop()

def reverse(string):
    n = len(string)
    stack = newStack()

    for i in range(n):
        push(stack,string[i])
    
    string = ''

    for i in range(n):
        string += pop(stack)
    
    return string

otherString = 'Decisions'

#print(reverse(otherString))

# Palindrome

def isPalindrome(input):
    if (len(input) == 0 or len(input) == 1):
        return True
    
    if (input[0] == input[len(input) - 1]):
        return isPalindrome(input[1:len(input) - 1])
    
    return False

print(isPalindrome('racecar'))

