import random
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            yield arr
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                yield arr


def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quick_sort(arr, low, high):
    if low < high:
        pivot = partition(arr, low, high)
        yield from quick_sort(arr, low, pivot - 1)
        yield from quick_sort(arr, pivot + 1, high)


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        yield from merge_sort(L)
        yield from merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            yield arr
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
            yield arr

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
            yield arr


def visualize_sorting(algorithm):
    array = [random.randint(1, 100) for _ in range(30)]
    generator = algorithm(array)

    fig, ax = plt.subplots()
    bars = ax.bar(range(len(array)), array)
    ax.set_title("Sorting Algorithm Visualization")

    def update(_):
        for rect, val in zip(bars, array):
            rect.set_height(val)

    FuncAnimation(fig, update, frames=generator, repeat=False, interval=50)
    plt.show()


def main():
    print("Sorting Algorithm Visualizer")
    print("1 - Bubble Sort")
    print("2 - Merge Sort")
    print("3 - Quick Sort")

    choice = input("Select algorithm: ").strip()

    if choice == "1":
        visualize_sorting(bubble_sort)
    elif choice == "2":
        visualize_sorting(merge_sort)
    elif choice == "3":
        arr = [random.randint(1, 100) for _ in range(30)]
        gen = quick_sort(arr, 0, len(arr) - 1)

        fig, ax = plt.subplots()
        bars = ax.bar(range(len(arr)), arr)
        ax.set_title("Quick Sort Visualization")

        def update(_):
            for rect, val in zip(bars, arr):
                rect.set_height(val)

        FuncAnimation(fig, update, frames=gen, repeat=False, interval=50)
        plt.show()
    else:
        print("Invalid choice")


if __name__ == "__main__":
    main()
