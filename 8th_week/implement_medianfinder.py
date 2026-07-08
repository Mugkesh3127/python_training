import heapq

class MedianFinder:

    def __init__(self):
        # Max-heap (store negative values)
        self.small = []

        # Min-heap
        self.large = []

    # -----------------------------
    # Add a number
    # -----------------------------
    def addNum(self, num):

        # Step 1: Add to max-heap
        heapq.heappush(self.small, -num)

        # Step 2: Ensure every element in small <= every element in large
        if self.large and (-self.small[0] > self.large[0]):
            value = -heapq.heappop(self.small)
            heapq.heappush(self.large, value)

        # Step 3: Balance heap sizes
        if len(self.small) > len(self.large) + 1:
            value = -heapq.heappop(self.small)
            heapq.heappush(self.large, value)

        elif len(self.large) > len(self.small):
            value = heapq.heappop(self.large)
            heapq.heappush(self.small, -value)

    # -----------------------------
    # Find Median
    # -----------------------------
    def findMedian(self):

        if len(self.small) > len(self.large):
            return -self.small[0]

        return (-self.small[0] + self.large[0]) / 2


# -----------------------------
# Test
# -----------------------------
mf = MedianFinder()

mf.addNum(1)
print(mf.findMedian())     # 1

mf.addNum(2)
print(mf.findMedian())     # 1.5

mf.addNum(3)
print(mf.findMedian())     # 2

mf.addNum(4)
print(mf.findMedian())     # 2.5

mf.addNum(5)
print(mf.findMedian())     # 3