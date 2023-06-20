from algo1 import *

def create_Set(array):
  arrLen = len(array)
  repElements = 0
  
  for i in range(0,arrLen):
    for j in range(i+1,arrLen):
      if array[j] != None and array[j] == array[i]:
        array[j] = None
        repElements += 1

  dimSet = arrLen - repElements
  setArr = Array(dimSet)

  j = 0
  for i in range(0, len(setArr)):
    
    while setArr[i] == None:
      
      setArr[i] = array[j]
      j += 1
  
  return setArr


def union(arrayS,arrayT):

  arraySValid = True
  arrayTValid = True
  
  if check_duplicates(arrayS) != '':
    print('Array S:', check_duplicates(arrayS))
    arraySValid = False
    
  if check_duplicates(arrayT) != '':
    print('Array T:', check_duplicates(arrayT))
    arrayTValid = False

  if arraySValid == True and arrayTValid == True:

    lenArrS = len(arrayS)
    lenArrT = len(arrayT)
    
    arrUnion = Array(lenArrS+lenArrT)

    for i in range(0,lenArrS):
      arrUnion[i] = arrayS[i]

    for i in range(0, lenArrT):
      arrUnion[lenArrS+i] = arrayT[i]

    setUnion = create_Set(arrUnion)
    return setUnion
    
  else:
    error = 'No es posible realizar union. Revise que los arrays sean TADs Sets.'
    return error
    

def intersection(arrayS,arrayT):
  arraySValid = True
  arrayTValid = True

  if check_duplicates(arrayS) != '':
    print('Array S:', check_duplicates(arrayS))
    arraySValid = False
    
  if check_duplicates(arrayT) != '':
    print('Array T:', check_duplicates(arrayT))
    arrayTValid = False

  if arraySValid == True and arrayTValid == True:

    lenArrS = len(arrayS)
    lenArrT = len(arrayT)

    sharedElementsTotal = 0
    
    for i in range(0,lenArrS):
      share = False
      for j in range(0,lenArrT):
        if arrayS[i] == arrayT[j]:
          share = True
          sharedElementsTotal += 1
      if share == False:
        arrayS[i] = None
    
    intersectArr = Array(sharedElementsTotal)

    j = 0
    for i in range(0, len(intersectArr)):
      while intersectArr[i] == None:
        if arrayS[j] != None:
          intersectArr[i] = arrayS[j]
        j += 1
      
    return intersectArr
    
  else:
    error = 'No es posible realizar interseccion. Revise que los arrays sean TADs Sets.'
    return error


def difference(arrayS, arrayT):
  arraySValid = True
  arrayTValid = True

  if check_duplicates(arrayS) != '':
    print('Array S:', check_duplicates(arrayS))
    arraySValid = False
    
  if check_duplicates(arrayT) != '':
    print('Array T:', check_duplicates(arrayT))
    arrayTValid = False

  if arraySValid == True and arrayTValid == True:
    lenArrS = len(arrayS)
    lenArrT = len(arrayT)

    onlySElements = 0
    
    for i in range(0,lenArrS):
      share = False
      for j in range(0,lenArrT):
        if arrayS[i] != None and arrayS[i] == arrayT[j]:
          share = True
          arrayS[i] = None
      if share == False:
        onlySElements += 1
        
    diffArr = Array(onlySElements)
    
    j = 0
    for i in range(0, len(diffArr)):
      while diffArr[i] == None:
        if arrayS[j] != None:
          diffArr[i] = arrayS[j]
        j += 1

    return diffArr

  else:
    error = 'No es posible realizar diferencia. Revise que los arrays sean TADs Sets.'
    return error

  
def check_duplicates(array):
  arrLen = len(array)
  repElements = 0
  
  for i in range(0,arrLen):
    for j in range(i+1,arrLen):
      if array[j] != None and array[j] == array[i]:
        repElements = 1

  if repElements == 1:
    error = 'Error: El array no es TAD Set'
    return error
  else:
    return ''
