import random
import matplotlib.pyplot as plt

time = 0  

def MergeSort(A, p, r):
    global time
    time = time + 1
    if p < r:
        q = (p + r) // 2
        MergeSort(A, p, q)
        MergeSort(A, q + 1, r)
        Merge(A, p, q, r)
    return time

def Merge(A, p, q, r):
    global time
    time = time + 1
    Left = A[p:q+1]
    Right = A[q+1:r+1]
    i = 0
    j = 0
    k = p
    
    while i < len(Left) and j < len(Right):
        time = time + 1
        if Left[i] < Right[j]:
            A[k] = Left[i]
            i += 1
        else:
            A[k] = Right[j]
            j += 1
        k += 1
    
    while i < len(Left):
        A[k] = Left[i]
        i += 1
        k += 1

    while j < len(Right):
        A[k] = Right[j]
        j += 1
        k += 1
    return time
#LISTA ORDENADA DESCENDENTE
if __name__ == "__main__":
    sizes = []
    times = []
    for size in range(1, 1000):
        lst = list(range(size, 0, -1)) 
        time = MergeSort(lst, 0, len(lst) - 1)
        sizes.append(size)
        times.append(time)
    
    plt.plot(sizes, times, marker='o')
    plt.title('Merge Sort (Lista Ordenada Inversa)')
    plt.grid(True)
    plt.show()
"""
#LISTA ALEATORIA
if __name__ == "__main__":
    sizes = []
    times = []
    for size in range(1, 1000):
        lst = [random.randint(-50, 50) for _ in range(size)]
        time = MergeSort(lst, 0, len(lst) - 1)
        sizes.append(size)
        times.append(time)
    
    plt.plot(sizes, times, marker='o')
    plt.title('Merge Sort.random')
    plt.grid(True)
    plt.show()
"""
