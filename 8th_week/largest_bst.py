import heapq

def find_kth_largest(nums, k):
    # Create a min-heap with the first k elements
    heap = nums[:k]
    heapq.heapify(heap)

    # Process the remaining elements
    for num in nums[k:]:
        if num > heap[0]:
            heapq.heapreplace(heap, num)

    # Root of the heap is the kth largest element
    return heap[0]


# -----------------------------
# Test
# -----------------------------
nums = [3, 2, 1, 5, 6, 4]
k = 2

print(f"{k}nd Largest Element:", find_kth_largest(nums, k))