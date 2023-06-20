from binarytree import *
import linkedlist

def treeFactory(stringsList,keysList):
    bt = BinaryTree()
    for i in range(len(keysList)):
        insert(bt,stringsList[i],keysList[i])
    return bt

strings1 = ['50','20','60','15','25','10','70']
keys1 = [50,20,60,15,25,10,70]

strings2 = ['20','15','25','10']
keys2 = [20,15,25,10]

bt1 = treeFactory(strings1,keys1)
bt2 = treeFactory(strings2,keys2)

# Ejercicio 1 - Funcion que verifica si un arbol binario es balanceado

def ejercicio1(root):
    if esBalanceado(root) == -1:
        print('No balanceado')
    else:
        print('Balanceado')

def esBalanceado(root):
    #Condicion base
    if root == None:
        return True
    
    alturaSubArbolIzq = esBalanceado(root.leftnode)

    if alturaSubArbolIzq == -1:
        return -1
    
    alturaSubArbolDer = esBalanceado(root.rightnode)

    if alturaSubArbolDer == -1:
        return -1
    
    if (abs(alturaSubArbolIzq - alturaSubArbolDer) > 1):
        return -1
    else:
        return max(alturaSubArbolDer,alturaSubArbolIzq) + 1

#ejercicio1(bt1.root)

# Ejercicio 2 - Determinar si un arbol BT2 es subarbol de un arbol BT1

def sonIguales(root1, root2):
    #Caso base
    if root1 == None and root2 == None:
        return True
    if root1 == None or root2 == None:
        return False

    return (root1.key == root2.key and sonIguales(root1.leftnode, root2.leftnode) and sonIguales(root1.rightnode, root2.rightnode))


def subArbol(rootBT1, rootBT2):
    # Caso base
    if rootBT2 == None:
        return True
    
    if rootBT1 == None:
        return False

    if (sonIguales(rootBT1, rootBT2)):
        return True

    return subArbol(rootBT1.leftnode, rootBT2) or subArbol(rootBT1.rightnode, rootBT2)


def ejercicio2(BT1,BT2):
    if subArbol(BT1.root, BT2.root):
        print('BT2 es subArbol de BT1')
    else:
        print('BT2 no es subArbol de BT1')

#ejercicio2(bt1,bt2)

# Ejercicio 3 - Determinar si un arbol binario es un arbol binario de busqueda

arbol = BinaryTree()
nodo1 = BinaryTreeNode()
nodo2 = BinaryTreeNode()
nodo3 = BinaryTreeNode()

nodo1.key = 30
nodo2.key = 10
nodo3.key = 80

arbol.root = nodo1
arbol.root.leftnode = nodo3
arbol.root.rightnode = nodo2

def checkBST(B):
    #Recorro el arbol binario In order
    listaInOrder = traverseInOrder(B)
    if listaInOrder == None:
        return False
    
    # Itero a traves de la lista.
    currentNode = listaInOrder.head
    while currentNode.nextNode != None:
        # Si la lista no esta ordenada forma creciente, luego el arbol no es BST
        if currentNode.value > currentNode.nextNode.value:
            return False
        currentNode = currentNode.nextNode
    return True

print(checkBST(arbol))