from linkedlist import *

miLista = LinkedList()
add(miLista,10)
add(miLista,24)
add(miLista,5)
add(miLista,78)

imprimirLista(miLista)

#Invertir Lista

def reverseList(list):
    newList = LinkedList
    current = list.head
    while current != None:
        add(newList,current.value)
        current = current.nextNode
    return newList

listaInvertida = reverseList(miLista)
imprimirLista(listaInvertida)

