import heapq


# Given an unsorted array of size k, find the k th largest element in it
def kth_largest_element(nums, k):
    """
    Approach for this solution has complexity O(n*log(k)) as at any iteration
    we maintain a min-heap of k largest elements seen so far
    """
    min_heap = []
    for num in nums:
        heapq.heappush(min_heap, num)
        if len(min_heap) > k:
            heapq.heappop(min_heap)
    return min_heap[0]


def heapify(arr, n, i):
    # Max-heap formation
    largest, left, right = i, 2 * i + 1, 2 * i + 2
    if left < n and arr[largest] < arr[left]:
        largest = left
    if right < n and arr[largest] < arr[right]:
        largest = right
    if largest != i:
        # swap arr[largest] and arr[i]
        arr[largest], arr[i] = arr[i], arr[largest]
        # ensure that all levels below largest are also sorted
        heapify(arr, n, largest)


def heapsort(nums, n):
    for i in range(n // 2, -1, -1):
        heapify(nums, n, i)
    print("After heap formation:", nums)
    # Extract elements from the heap one by one
    for i in range(n - 1, 0, -1):
        # Swap the root (largest element) with the last element
        nums[0], nums[i] = nums[i], nums[0]
        # Reduce the heap size and heapify the root
        heapify(nums, i, 0)
    print("After heap sort:", nums)


if __name__ == "__main__":
    nums, k = [-1, 13, 2, 1, 5, 6, 4], 2
    print("k th largest element is:", kth_largest_element(nums, k))
    # Insert 1: Heap remains [2, 3] (no change, as 1 < 2).
    # Insert 5: Replace 2 → Heap becomes [3, 5] (cost O(logk)).
    # Insert 6: Replace 3 → Heap becomes [5, 6] (cost O(logk)).
    # Insert 4: Ignored, as 4 < 5
    # Final heap: [5, 6] ==> return 5
    n = len(nums)
    heapsort(nums, n)
