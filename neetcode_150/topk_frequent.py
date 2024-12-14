from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Use Counter to count frequencies of elements in nums
        freq_map = Counter(nums)
        
        # Sort the items by frequency in descending order
        sorted_items = sorted(freq_map.items(), key=lambda x: x[1], reverse=True)
        
        # Extract the top k keys
        return [item[0] for item in sorted_items[:k]]
        

if __name__ == "__main__":

    # answer is [2,3]
    topKFrequent([1,2,2,3,3,3], 2)