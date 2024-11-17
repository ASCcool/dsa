# Non-adaptive, Non-stable, O(n^2) always
def selection(arr, n):
    # Lowest number of swaps
    for i in range(0, n):
        j_min, low = -1, 1000000
        for j in range(i, n):
            if arr[j] < low:
                j_min, low = j, arr[j]
        # swap arr[j_min] and arr[i]
        temp = arr[j_min]
        arr[j_min] = arr[i]
        arr[i] = temp
        print(f"After {i}th pass with j_min:{j_min} and low:{low}, array is:", arr)
    print(arr)


# Non-adaptive by default but can be made adaptive, Stable, O(n^2) always
def bubble(arr, n):
    # Largest number of comparisons and swaps in all iterations
    for i in range(n - 1, 0, -1):
        swapped = 0
        for j in range(0, i):
            if arr[j + 1] < arr[j]:
                swapped = 1
                # swap arr[j+1] and arr[j]
                temp = arr[j + 1]
                arr[j + 1] = arr[j]
                arr[j] = temp
        # Making bubble sort adaptive
        if swapped == 0:
            # Array is already sorted
            print("Array is already sorted, hence breaking loop")
            break
        print(f"After {n - i}th pass:", arr)
    print(arr)


# Adaptive, Stable, O(n), O(n^2)
def insertion(arr, n):
    for i in range(1, n):
        j, ele = i, arr[i]
        while j >= 1 and arr[j - 1] > ele:
            # shift elements to the right, no swapping
            arr[j] = arr[j - 1]
            j -= 1
        arr[j] = ele
        print(f"After {i}th pass:", arr)
    print(arr)


# Not adaptive, Unstable, Average and best - O(n*log n) and worst - O(n^2),
# In-place so no extra space and works better for small arrays
def quicksort(arr, low, high):
    def partition(arr, low, high):
        pivot = arr[low]
        i = low + 1
        j = high
        while True:
            # find i for which arr[i] is greater than pivot
            while i <= high and arr[i] < pivot:
                i += 1
            # find j for which arr[j] is less than or equal to pivot
            while j > low and arr[j] >= pivot:
                j -= 1
            # Check if the pointers crossed, if so, break out of the loop
            if i >= j:
                break
            # swap arr[i] with arr[j]
            temp = arr[j]
            arr[j] = arr[i]
            arr[i] = temp

        # swap pivot with arr[j]
        temp = pivot
        arr[low] = arr[j]
        arr[j] = temp
        return j

    if low < high:
        # pehle main array partition ke according sort hoga then right and left subarrays
        partitionindex = partition(arr, low, high)
        print(f"After middle partition with pivot index: {partitionindex}, arr:", arr)
        quicksort(arr, low, partitionindex - 1)
        quicksort(arr, partitionindex + 1, high)

    print("Final sorted array:", arr)


# Not adaptive, Stable, O(n*log n) always, requires extra space and works best for large arrays
def mergesort(arr, low, high):
    def merge(arr, low, mid, high):
        # low to mid and mid+1 to high
        new = [-1] * (high - low + 1)
        i, j, k = low, mid + 1, 0
        while i <= mid and j <= high:
            if arr[i] <= arr[j]:
                new[k] = arr[i]
                i += 1
                k += 1
            else:
                new[k] = arr[j]
                j += 1
                k += 1
        while i <= mid:
            new[k] = arr[i]
            i += 1
            k += 1
        while j <= high:
            new[k] = arr[j]
            j += 1
            k += 1
        # Copy back new array to old array slice
        for var in range(low, high + 1):
            arr[var] = new[var - low]
        # shortcut via python slicing
        # arr[low:high+1] = new

    if low < high:
        mid = low + (high - low) // 2
        # pehle right and left subarray sort and merge honge fir main array
        mergesort(arr, low, mid)
        mergesort(arr, mid + 1, high)
        merge(arr, low, mid, high)


if __name__ == "__main__":
    arr = [4, 7, 3, -1, 0, 6, 2, 1, 9, 9]
    # arr = [7, 9, 18, 19, 22, 1, 6, 9, 11]
    n = len(arr)
    # bubble(arr, n)
    # insertion(arr, n)
    # selection(arr, n)
    # quicksort(arr, 0, n-1)
    mergesort(arr, 0, n - 1)
    print(arr)
