import heapq

# -----------------------------
# Min Heap
# -----------------------------
print("----- Min Heap -----")

min_heap = []

# Insert elements
heapq.heappush(min_heap, 10)
heapq.heappush(min_heap, 5)
heapq.heappush(min_heap, 20)
heapq.heappush(min_heap, 8)

print("Heap:", min_heap)
print("Smallest element:", min_heap[0])

print("Elements in sorted order:")
while min_heap:
    print(heapq.heappop(min_heap), end=" ")

print("\n")


# -----------------------------
# Max Heap
# -----------------------------
print("----- Max Heap -----")

max_heap = []

# Insert negative values
heapq.heappush(max_heap, -10)
heapq.heappush(max_heap, -5)
heapq.heappush(max_heap, -20)
heapq.heappush(max_heap, -8)

print("Heap (stored as negatives):", max_heap)
print("Largest element:", -max_heap[0])

print("Elements in descending order:")
while max_heap:
    print(-heapq.heappop(max_heap), end=" ")

print("\n")


# -----------------------------
# MaxHeap Class
# -----------------------------
class MaxHeap:
    def __init__(self):
        self.heap = []

    def push(self, value):
        heapq.heappush(self.heap, -value)

    def pop(self):
        if self.heap:
            return -heapq.heappop(self.heap)
        return None

    def peek(self):
        if self.heap:
            return -self.heap[0]
        return None

    def size(self):
        return len(self.heap)

    def is_empty(self):
        return len(self.heap) == 0


# -----------------------------
# Test MaxHeap Class
# -----------------------------
print("----- MaxHeap Class -----")

h = MaxHeap()

for num in [10, 5, 20, 8]:
    h.push(num)

print("Top element:", h.peek())
print("Size:", h.size())

print("Removing elements:")
while not h.is_empty():
    print(h.pop(), end=" ")