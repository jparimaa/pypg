import quicksort
import mergesort
import random
import datetime

def is_sorted(values):
    for i in range(len(values) - 2):
        if i > values[i + 1]:
            return False
    return True

def run_sort(func, text):
    start = datetime.datetime.now()
    func()
    end = datetime.datetime.now()
    assert is_sorted(quicksort_list)
    execution_time_ms = (end - start).microseconds / 1000.0
    print("{}, N = {} in {} milliseconds".format(text, len(my_list), execution_time_ms))
    
my_list = []
for i in range(1000):
    my_list.append(i)

random.shuffle(my_list)

quicksort_list = my_list.copy()
quicksort_func = lambda : quicksort.sort(quicksort_list, 0, len(quicksort_list) - 1)
run_sort(quicksort_func, "Quicksort")

mergesort_list = my_list.copy()
mergesort_func = lambda : mergesort.sort(mergesort_list)
run_sort(mergesort_func, "Mergesort")
