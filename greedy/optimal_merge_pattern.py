import heapq

# A good example of this is merging two sorted lists, assume you have n such lists 
# and you want to merge all of them (2 at once) for lowest cost, where cost = O(m+n)
def optimalMergePattern(file_sizes):
    # Create a min-heap from file sizes
    heapq.heapify(file_sizes)
    total_cost = 0

    # While more than one file remains
    while len(file_sizes) > 1:
        # Extract the two smallest files
        first = heapq.heappop(file_sizes)
        second = heapq.heappop(file_sizes)

        # Merge them
        cost = first + second
        total_cost += cost

        # Push the merged file back into the heap
        heapq.heappush(file_sizes, cost)

    return total_cost

if __name__ == "__main__":
    # Test
    file_sizes = [4, 3, 2, 6]
    print("Optimal merge cost:", optimalMergePattern(file_sizes))  # Output: 29