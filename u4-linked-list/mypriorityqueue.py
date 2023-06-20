from linkedlist import *
from mystack import *

class PriorityQueue:
  head = None

class PriorityNode:
  value = None
  nextNode = None
  priority = None

def enqueue_priority(Q,element,priority):
  currentPos = 0
  currentNode = Q.head
  prevNode = None

  if currentNode == None:
    newNode = PriorityNode()
    newNode.value = element
    newNode.priority = priority
    Q.head = newNode
    return currentPos

  newNode = PriorityNode()
  newNode.value = element
  newNode.priority = priority
  
  while currentNode != None:
    if priority > currentNode.priority:
      
      if currentPos != 0:
        prevNode.nextNode = newNode
        
      if currentPos == 0:
        Q.head = newNode
    
      newNode.nextNode = currentNode
      currentNode = newNode
      return currentPos
      
    elif currentNode.nextNode == None:
      currentNode.nextNode = newNode
      return currentPos + 1
      
    prevNode = currentNode
    currentNode = currentNode.nextNode
    currentPos += 1
  return

def dequeue_priority(Q):
  return pop(Q)