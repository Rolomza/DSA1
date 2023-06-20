from bHeap import *
import linkedlist

def HeapSort(L):
	if(L.head != None):
		bHeap = Bheap()
		heapify(bHeap, L)
		L.head = None
		HeapSortRecursivo(bHeap, L, linkedlist.length(bHeap.bheaplist))

def HeapSortRecursivo(Bheap, L, size):
	k = delMax(Bheap)
	linkedlist.add(L, k)
	shiftDown(Bheap, 1)
	if(size > 2):
		HeapSortRecursivo(Bheap, L, size - 1)

lista = linkedlist.LinkedList()
linkedlist.add(lista, 66)
linkedlist.add(lista, 72)
linkedlist.add(lista, 20)
linkedlist.add(lista, 12)
linkedlist.add(lista, 47)

print('lista original')
linkedlist.imprimirLista(lista)
HeapSort(lista)
print('lista ordenada')
linkedlist.imprimirLista(lista)