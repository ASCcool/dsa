# Equivalent of ordered map container (map <int, int>) in C++
from sortedcontainers import SortedDict

# Use Counter to count frequencies of elements in nums
from collections import Counter
freq_map = Counter(nums)

# Sort the items in a dict by value in descending order
sorted_items = sorted(freq_map.items(), key=lambda x: x[1], reverse=True)

# Maintains order in which elements are inserted in the dict
# Python 3.7 and above by default maintain order and dict is faster than ordered dict
from collections import OrderedDict

# Equivalent of ordered set container (set <int>) in C++
use OrderedDict/dict (Python 3.7+) and just get the keys

# Add items to a set in python
s = set()
s.add(2)