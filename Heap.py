# Heapq  Module:
import heapq

# min-heap: heap[0] -> the smallest
# the heap will return or pop the smallest or largest while make the heap structure the same

# LC: 215. Kth Largest Element in an Array
def findKthLargest(self, nums, k):
  heap = []
  for num in nums:
    heapq.heappush(heap, num)
    if len(heap)>k:
      heapq.heappop(heap)
  return heap[0]
