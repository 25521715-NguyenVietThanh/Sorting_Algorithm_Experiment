import numpy as np
import time
import sys

sys.setrecursionlimit(2000000)

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and arr[i] < arr[l]:
        largest = l
    if r < n and arr[largest] < arr[r]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)
    arr_list = arr.tolist() if isinstance(arr, np.ndarray) else arr
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr_list, n, i)
    for i in range(n - 1, 0, -1):
        arr_list[i], arr_list[0] = arr_list[0], arr_list[i]
        heapify(arr_list, i, 0)
    return arr_list

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    arr_list = arr.tolist() if isinstance(arr, np.ndarray) else arr
    pivot = arr_list[len(arr_list) // 2]
    left = [x for x in arr_list if x < pivot]
    middle = [x for x in arr_list if x == pivot]
    right = [x for x in arr_list if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

n = 1000000
datasets = []

datasets.append(np.sort(np.random.rand(n)))
datasets.append(np.sort(np.random.rand(n))[::-1])
for _ in range(3):
    datasets.append(np.random.rand(n))
for _ in range(5):
    datasets.append(np.random.randint(0, 1000000, n))

labels = ["Day tang dan", "Day giam dan", "Day thuc ngau nhien 1", "Day thuc ngau nhien 2", "Day thuc ngau nhien 3",
          "Day nguyen ngau nhien 1", "Day nguyen ngau nhien 2", "Day nguyen ngau nhien 3", "Day nguyen ngau nhien 4", "Day nguyen ngau nhien 5"]

algorithms = {
    "NumPy Sort": np.sort,
    "QuickSort": quick_sort,
    "HeapSort": heap_sort,
    "MergeSort": merge_sort
}

results = {}

for alg_name in algorithms:
    alg_times = []
    for i in range(10):
        data_copy = datasets[i].copy()
        start = time.time()
        algorithms[alg_name](data_copy)
        end = time.time()
        duration_ms = (end - start) * 1000
        alg_times.append(round(duration_ms, 2))
    results[alg_name] = alg_times

print("\nKET QUA THOI GIAN CHAY (ms):")
print(f"{'Ten day du lieu':<25} | {'NumPy':<12} | {'Quick':<12} | {'Heap':<12} | {'Merge':<12}")
print("-" * 80)
for i in range(10):
    print(f"{labels[i]:<25} | {results['NumPy Sort'][i]:<12} | {results['QuickSort'][i]:<12} | {results['HeapSort'][i]:<12} | {results['MergeSort'][i]:<12}")