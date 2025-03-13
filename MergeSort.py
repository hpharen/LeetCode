def merge_sort(arr):
    if len(arr) > 1:
        array1 = arr[:len(arr)//2]
        array2 = arr[len(arr)//2:]

        # recursion
        merge_sort(array1)
        merge_sort(array2)

        # merge
        i = 0 # left array index
        j = 0 # right array index
        k = 0 # merged array index
        while i < len(array1) and j < len(array2):
            if array1[i] < array2[j]:
                arr[k] = array1[i]
                i += 1
            else:
                arr[k] = array2[j]
                j += 1
            k += 1
        
        while i < len(array1):
            arr[k] = array1[i]
            i += 1
            k += 1

        while j < len(array2):
            arr[k] = array2[j]
            j += 1
            k += 1


arr_test = [2, 3, 4, 1, 7, 8, 9, 10, 2, 5, 76, 2, 6]
merge_sort(arr_test)
print(arr_test)