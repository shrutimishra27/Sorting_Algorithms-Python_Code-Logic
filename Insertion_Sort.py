# 4. INSERTION SORT
def insertionsort(array):
    for i in range(1,len(array)):
        celement = array[i]                    #celement=current element(to be compared)

        while celement < array[i-1] and i>0:
            array[i] = array[i-1]
            i = i - 1 
        array[i] = celement 

array = [15,36,12,65,57,40,73,29]
print("The unsorted array is : ",array)
insertionsort(array)
print("The sorted array is : ", array)