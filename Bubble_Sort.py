# 2. BUBBLE SORT
def bubblesort(array):
    for j in range(len(array)-1):              #Elements are n, So total comparison will be n-1
        for i in range(len(array)-1):          #Elements are n, So total paas will be n-1
            if array[i] > array[i+1]:          #Compare adjacent elements.
                array[i] , array[i+1] = array[i+1] , array[i]
    
array = [15,36,12,65,57,40,73,29]
print("The unsorted array is : ",array)
bubblesort(array)
print("The sorted array is : ", array)