import random
import matplotlib.pyplot as plt

time = 0

def heap_sort(arr):
    global time
    time += 1
    build_max_heap(arr)
    heap_size = len(arr)
    
    while heap_size > 1:
        time += 1
        arr[0], arr[heap_size - 1] = arr[heap_size - 1], arr[0]
        max_heapify(arr, heap_size - 1, 0)
        heap_size -= 1

def max_heapify(arr, heap_size, idx):
    global time
    time += 1
    largest = idx
    left = 2 * idx + 1
    right = 2 * idx + 2
    
    if left < heap_size and arr[idx] < arr[left]:
        largest = left
    if right < heap_size and arr[largest] < arr[right]:
        largest = right
        
    if largest != idx:
        arr[idx], arr[largest] = arr[largest], arr[idx]
        max_heapify(arr, heap_size, largest)

def build_max_heap(arr):
    global time
    time += 1
    heap_len = len(arr)
    i = heap_len // 2
    while i >= 0:
        time += 1
        max_heapify(arr, heap_len, i)
        i -= 1

if __name__ == "__main__":
    sizes = []
    times = []
    for size in range(1, 1000):
        lst = list(range(size,0,-1))        
        #print("Original List:", lst)        
        time = 0
        heap_sort(lst)
        #print("Sorted List:", lst)        
        sizes.append(size)
        times.append(time)
    
    plt.plot(sizes, times, marker='o')
    plt.title('Heap Sort (Random List)')
    plt.xlabel('List Size')
    plt.ylabel('Time Complexity')
    plt.grid(True)
    plt.show()
