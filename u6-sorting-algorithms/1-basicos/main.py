from linkedlist import *

lista = LinkedList()
add(lista, 3)
add(lista, 1)
add(lista, 6)
add(lista, 4)
add(lista, 2)
add(lista, 5)


# Bubble Sort

def bubbleSort(L):
    lenList = length(L)
    for i in range(lenList):
        currentNode = L.head
        n = 0
        while currentNode.nextNode != None:
            if currentNode.value > currentNode.nextNode.value:
                move(L,n,n+1)
            else:
                currentNode = currentNode.nextNode
            n += 1

def pruebaBubbleSort(lista):
    print('Algoritmo BubbleSort')
    print('Lista original')
    imprimirLista(lista)
    bubbleSort(lista)
    print('Lista ordenada')
    imprimirLista(lista)


# Selection Sort

def selectionSort(L):
    lenList = length(L)
    for i in range(lenList):
        menorVal = access(L,i)
        menorPos = i
        for j in range(i+1,lenList):
            if access(L,j) < menorVal:
                menorPos = j
        move(L,menorPos,i)

def pruebaSelectionSort(L):
    print('Algoritmo SelectionSort')
    print('Lista original')
    imprimirLista(L)
    selectionSort(L)
    print('Lista ordenada')
    imprimirLista(L)

# Insertion sort

def insertionSort(L):
    lenList = length(L)
    for i in range(1,lenList):
        key = access(L,i)
        j = i - 1
        while j > -1 and access(L,j) > key:
            j = j - 1
        move(L,i,j+1)

def pruebaInsertionSort(L):
    print('Algoritmo InsertionSort')
    print('Lista original')
    imprimirLista(L)
    insertionSort(L)
    print('Lista ordenada')
    imprimirLista(L)

#pruebaBubbleSort(lista)
#pruebaSelectionSort(lista)
#pruebaInsertionSort(lista)
