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
            values[lower], values[upper] = values[upper], values[lower]
    values[first], values[upper] = values[upper], values[first]
    return upper