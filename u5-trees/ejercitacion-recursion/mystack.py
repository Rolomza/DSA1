from linkedlist import *

def push(S,element):
  add(S,element)

def pop(S):
  firstElement = S.head
  if firstElement != None:
    S.head = firstElement.nextNode
    return firstElement.value
  return
