def sort(input):
    if len(input) > 1:
        mid = len(input) // 2
        left_array = input[:mid]
        right_array = input[mid:]
 
        sort(left_array)
        sort(right_array)
 
        i, j, k = 0, 0, 0
 
        while i < len(left_array) and j < len(right_array):
            if left_array[i] < right_array[j]:
                input[k] = left_array[i]
                i += 1
            else:
                input[k] = right_array[j]
                j += 1
            k += 1
 
        while i < len(left_array):
            input[k] = left_array[i]
            i += 1
            k += 1
 
        while j < len(right_array):
            input[k] = right_array[j]
            j += 1
            k += 1
