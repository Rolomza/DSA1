from algo1 import *

def search(Array, element):
  indexElement = None
  i = 0
  while i < len(Array) and indexElement == None:
    if Array[i] == element:
      indexElement = i
    i += 1

  return indexElement


def insert(Array, element, position):

  indexInserted = None

  if position > len(Array) - 1 or position < 0:
    indexInserted = None
    
  else:

    for i in range(len(Array) - 1, position, -1):
      Array[i] = Array[i - 1]
    
    Array[position] = element
    indexInserted = position
  
  return indexInserted
  
  
def delete(Array, element):
  
  indexDeleted = None

  for i in range(0, len(Array)):

    if Array[i] == element and indexDeleted == None:
      for n in range(i, len(Array)-1):
        Array[n] = Array[n+1]

      Array[len(Array) -1] = None
      indexDeleted = i

  return indexDeleted
  

def length(Array):
  activeElements = 0
  for i in range(0,len(Array)):
    if Array[i] != None:
      activeElements += 1

  return activeElements