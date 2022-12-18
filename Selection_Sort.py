# 5. SELECTION SORT
def selectionsort(array):
    for i in range(len(array)):
        min_val = min(array[i:])
        ind_min = array.index(min_val)
        array[i] , array[ind_min] = array[ind_min] , array[i]

array = [15,36,12,65,57,40,73,29]
print("The unsorted array is : ",array)
selectionsort(array)
print("The sorted array is   : ", array)