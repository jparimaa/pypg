def sort(input, first, last):
    if first >= last:
        return
    pivotindex = partition(input, first, last)
    sort(input, first, pivotindex - 1)
    sort(input, pivotindex + 1, last)
  
def partition(values, first, last):
    pivotvalue = values[first]
    lower = first + 1
    upper = last
    done = False
    while not done:
        while lower <= upper and values[lower] <= pivotvalue:
            lower += 1
        while values[upper] >= pivotvalue and upper >= lower:
            upper -= 1
        if upper < lower:
            done = True
        else:
            values[lower], values[upper] = swap(values[lower], values[upper])
    values[first], values[upper] = swap(values[first], values[upper])
    return upper

def swap(s1, s2):
    return s2, s1