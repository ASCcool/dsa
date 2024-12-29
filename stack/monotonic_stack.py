def next_greatest_element(arr, traversal="right"):
    n = len(arr)
    nge = [-1] * n  # Initialize result array with -1
    stack = []  # Monotonic stack
    # Traverse the array
    _range = range(n - 1, -1, -1) if traversal == "right" else range(0, n)
    for i in _range:
        print("arr[i]:", arr[i], "stack:", stack)
        # Pop elements from stack while they are less than or equal to the current element
        while stack and stack[-1] <= arr[i]:
            stack.pop()
        # If stack is not empty, the top of the stack is the next greatest element
        if stack:
            nge[i] = stack[-1]
        # Push the current element onto the stack
        stack.append(arr[i])
    return nge


def next_smallest_element(arr, traversal="right"):
    n = len(arr)
    nse = [-1] * n  # Initialize result array with -1
    stack = []  # Monotonic stack
    # Traverse the array
    _range = range(n - 1, -1, -1) if traversal == "right" else range(0, n)
    for i in _range:
        print("arr[i]:", arr[i], "stack:", stack)
        # Pop elements from stack while they are greater than or equal to the current element
        while stack and stack[-1] >= arr[i]:
            stack.pop()
        # If stack is not empty, the top of the stack is the next smallest element
        if stack:
            nse[i] = stack[-1]
        # Push the current element onto the stack
        stack.append(arr[i])
    return nse


if __name__ == "__main__":
    array = [1, -1, 0, 3, 2, 1, 5, 7]
    print("NGE right:", next_greatest_element(array), "\n")
    print("NGE left:", next_greatest_element(array, "left"), "\n")
    print("NSE right:", next_smallest_element(array), "\n")
    print("NSE left:", next_smallest_element(array, "left"), "\n")
