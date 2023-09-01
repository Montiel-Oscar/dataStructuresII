import random
import matplotlib.pyplot as plt

time = 0

def quick_sort(lst, low, high):
    global time
    time += 1
    if low < high:
        pivot, time = partition(lst, low, high, time)
        quick_sort(lst, low, pivot - 1)
        quick_sort(lst, pivot + 1, high)
    
    return time

def partition(lst, low, high, time):
    time += 1
    i = low - 1
    pivot_index = (low + high) // 2 ## pivote en el medio 
    pivot = lst[pivot_index]
    lst[pivot_index], lst[high] = lst[high], lst[pivot_index]  # Movemos el pivote al final
    j = low
    
    while j < high:
        time += 1
        if lst[j] <= pivot:
            i += 1
            lst[i], lst[j] = lst[j], lst[i]
        j += 1
    
    lst[i + 1], lst[high] = lst[high], lst[i + 1]
    return (i + 1), time

if __name__ == "__main__":
    sizes = []
    times = []
    for size in range(1, 1000):
        lst = list(range(1, size + 1))  # Lista ordenada
        quick_sort(lst, 0, len(lst) - 1)
        sizes.append(size)
        times.append(time)
        time = 0
    
    plt.plot(sizes, times, marker='o')
    plt.title('Quick Sort (Best Case: Sorted List with Pivot in Middle)')
    plt.xlabel('List Size')
    plt.ylabel('Time Complexity')
    plt.grid(True)
    plt.show()
