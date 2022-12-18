# 3. MERGE SORT
def mergesort(array):
    if len(array) > 1:              #Splitting into 2 parts
        mid = len(array) // 2
        larray = array[:mid]
        rarray = array[mid:]
        mergesort(larray)           #Splitting left array
        mergesort(rarray)           #Splitting right array
        
        i=j=k=0
        
        while i < len(larray) and j < len(rarray):
            if larray[i] < rarray[j]:
                array[k] = larray[i]
                i = i + 1
                k = k + 1
            else:
                array[k] = rarray[j]
                j = j + 1
                k = k + 1
        while i < len(larray):       #If any element left in left array.
            array[k] = larray[i]
            i = i + 1
            k = k + 1
        while j < len(rarray):      #If any element left in right array.
            array[k] = rarray[j]
            j = j + 1
            k = k + 1
     
array = [15,36,12,65,57,40,73,29]
print("The unsorted array is : ",array)
mergesort(array)
print("The sorted array is : ", array)