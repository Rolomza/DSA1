from tempfile import TemporaryDirectory
from linkedlist import *
from mystack import *
from algo1 import *

print('Bubble sort algorithm')

# def bubbleSort(arr):
#     n = len(arr)
#     sorted = False

#     while not sorted:
#         sorted = True
#         for i in range(0, n-1):
#             if arr[i] > arr[i+1]:
#                 sorted = False
#                 arr[i] , arr[i+1] = arr[i+1] , arr[i]
#     return arr

# arrayTest = [2,5,1]
# bubbleSort(arrayTest)
# print('Sorted Array:')
# for i in range(len(arrayTest)):
#     print(arrayTest[i], end=" ")

# EJERCICIO 4 - Ordenar lista enlazada de menor a mayor

miLista = LinkedList()

add(miLista,2)
add(miLista,1)
add(miLista,13)
add(miLista,3)
add(miLista,5)
add(miLista,9)
add(miLista,4)

imprimirLista(miLista)

def move(linkedList,position_orig,position_dest):
    nodesAmount = length(linkedList)
    indexLength = nodesAmount - 1

    if position_orig >= 0 and position_orig <= indexLength:
        if position_dest >= 0 and position_dest <= indexLength:
            originValue = access(linkedList,position_orig)
            destinyValue = access(linkedList,position_dest)
            tempVar = destinyValue
            update(linkedList,originValue,position_dest)
            update(linkedList,tempVar,position_orig)
            return 
        else:
            return 'Error index position_dest'
    else:
        return 'Error index position_orig'


def ordenarListaMenorAMayor(lista,nodoActual,isSorted,swapped):

  current = nodoActual
  nextNode = current.nextNode

  # Caso base
  if isSorted == False and swapped == True:
    swapped = False
    return ordenarListaMenorAMayor(lista,lista.head,isSorted,swapped)
  elif isSorted == True and nextNode == None:
    return 
  else:
    # Caso general
    isSorted = True
    swapped = False
    if current.value > nextNode.value:
      isSorted = False
      swapped = True
      positionCurrent = search(lista,current.value)
      positionNextNode = search(lista,nextNode.value)
      move(lista,positionCurrent,positionNextNode)
    
    return ordenarListaMenorAMayor(lista,nextNode,isSorted,swapped)

ordenarListaMenorAMayor(miLista,miLista.head,False,False)

imprimirLista(miLista)




