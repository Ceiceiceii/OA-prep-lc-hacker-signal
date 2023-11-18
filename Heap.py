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


#LC: 2336. Smallest Number in Infinite Set
class SmallestInfiniteSet(object):

    def __init__(self):
        self.current = 1 #heap[0] initially is 1
        self.heap = []

    def popSmallest(self):
        """
        :rtype: int
        """
        if len(self.heap)!=0:
            return heapq.heappop(self.heap)
        else:
            self.current +=1
            return self.current-1

    def addBack(self, num):
        """
        :type num: int
        :rtype: None
        """
        if num < self.current-1 and num not in self.heap:
            heapq.heappush(self.heap,num)
        elif num == self.current-1:
            self.current = num

