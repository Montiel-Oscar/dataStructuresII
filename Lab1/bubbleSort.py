import random
import matplotlib.pyplot as plt

def bubble_sortgraph(arr):

    time = 0    # 3
    n = len(arr)# 3
    i = 0       # 3
    while i < n:# 3n
        time += 1#4n   
        swapped = False#3n
        j = 0   #3n
        while j < n - i - 1: #n*((n-1)/2)+1
            time += 1        #4(n*((n-1)/2))
            if arr[j] > arr[j + 1]:#4(n*((n-1)/2))
                arr[j], arr[j + 1] = arr[j + 1], arr[j]#(n*((n-1)/2))
                swapped = True #3(n*((n-1)/2))
            j += 1 #4(n*((n-1)/2))
        if not swapped:#3n
            break#n
        i += 1#4n
    return time#
##f(n) = (1/2)(21n^2+21n+22) -> O(n^2)

if __name__ == "__main__":
    sizes = []
    times = []
    for size in range(1, 1000):
        lst = list(range(size, 0, -1))
        time = bubble_sortgraph(lst)  
        sizes.append(size)
        times.append(time)
        
    plt.plot(sizes, times, marker='o')
    plt.xlabel('Tamaño de la lista')
    plt.ylabel('Tiempo de ejecución')
    plt.title('Lista ordenada inversa')
    plt.grid(True)
    plt.show()
