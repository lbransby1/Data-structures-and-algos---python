def bubbleSort(array):

  for i in range (len(array)):            ## loop to access each array element
    for j in range(0, len(array) -i -1):  ## loop to compare array elements
      if array[j] > array[j+1]:           ##compare and swap
        temp = array[j]                  
        array[j] = array[j+1]
        array[j+1] = temp

data = [-4,-6,-26, 4, 26, 2475,27, 25, 78]
bubbleSort(data)
print(data)


#time complexity - best = O n, worst = O n^2, avg = O n^2
#space complexity = O 1

