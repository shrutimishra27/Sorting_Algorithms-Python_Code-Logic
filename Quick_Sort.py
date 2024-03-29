# 1. QUICK SORT
def Partition(array,low,high):
    i= low + 1
    j= high
    pivot = array[low]
    
    while True:
        while i <= high and array[i] <= pivot:
            i = i + 1
        while i <= high and array[j] >= pivot:
            j = j - 1
        if j < i:
            break
        else:
            array[i] ,array[j] = array[j] , array[i]
    array[low] , array[j] = array[j] , array[low]
    return j

def quicksort(array,low,high):
    if low < high:
        PartitonPos = Partition(array,low,high)
        quicksort(array,low,PartitonPos - 1)
        quicksort(array,PartitonPos + 1,high)
        
array = [15,36,12,65,57,40,73,29]
print("The unsorted array is : ",array)
quicksort(array,0,len(array)-1)
print("The sorted array is : ",array)