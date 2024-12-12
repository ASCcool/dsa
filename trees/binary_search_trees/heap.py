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


if __name__ == "__main__":
    nums, k = [3, 2, 1, 5, 6, 4], 2
    print(kth_largest_element(nums, k))
    # Insert 1: Heap remains [2, 3] (no change, as 1 < 2).
    # Insert 5: Replace 2 → Heap becomes [3, 5] (cost O(logk)).
    # Insert 6: Replace 3 → Heap becomes [5, 6] (cost O(logk)).
    # Insert 4: Ignored, as 4 < 5
    # Final heap: [5, 6] ==> return 5
