import quicksort
import mergesort
import bubblesort

import random
import datetime

import matplotlib.pyplot as plt
import numpy as np

def is_sorted(values):
    for i in range(len(values) - 2):
        if i > values[i + 1]:
            return False
    return True

def run_sort(func, list):
    list_copy = my_list.copy()
    start = datetime.datetime.now()
    func(list_copy)
    end = datetime.datetime.now()
    assert is_sorted(list_copy)
    list_copy.clear()
    execution_time_ms = (end - start).microseconds / 1000.0
    return execution_time_ms
    
def print_executions_time(text, n, time):
    print("{}, N = {} in {} milliseconds".format(text, n, time))

N = 500
my_list = []
for i in range(N):
    my_list.append(i)

random.shuffle(my_list)

quicksort_func = lambda list : quicksort.sort(list, 0, len(list) - 1)
quicksort_time = run_sort(quicksort_func, my_list)
print_executions_time("Quicksort", N, quicksort_time)

mergesort_func = lambda list : mergesort.sort(list)
mergesort_time = run_sort(mergesort_func, my_list)
print_executions_time("Mergesort", N, mergesort_time)

bubblesort_func = lambda list : bubblesort.sort(list)
bubblesort_time = run_sort(bubblesort_func, my_list)
print_executions_time("Bubblesort", N, bubblesort_time)

times = [quicksort_time, mergesort_time, bubblesort_time]
x = np.arange(len(times))
plt.title("Execution time in milliseconds, N = {}".format(N))
plt.bar(x, times)
plt.xticks(x, ('Quicksort', 'Mergesort', 'Bubblesort'))
plt.show()