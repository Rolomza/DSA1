# Insertion Sort

array1 = [1,5,7,2,9,3]

def bubbleSort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(0,n-i-1):
            if arr[j] > arr[j+1]:
                aux = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = aux

print('Array original')
print(array1)
print('Array ordenado')
bubbleSort(array1)
print(array1)