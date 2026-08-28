class MedianFinder:
    '''
    You can use a list with inorder insertion, but the efficient way is to use heap
    - We will maintain two heaps: small as a maxheap, and large as a minheap
    - Python only supports minheap out of box, so we have to multiply all numbers by -1 to achieve a maxheap
    - Insertion will be to the small heap by default
    - We will do two check after an insertion:
       - Making sure that values are in appropriate category
       - Ensuring that both heap are equally balance, or we will have to pop an element and push it to the other.
    '''

    def __init__(self):
        # create the two heap
        self.small_heap = []
        self.large_heap = []

    def addNum(self, num: int) -> None:
        # insert in small heap or large heap based on value
        if self.small_heap and num <= -1 * self.small_heap[0]:
            heapq.heappush(self.small_heap, -1 * num) # multiply due to maxheap workaround
        else:
            heapq.heappush(self.large_heap, num)

        # check: small heap is not too bigger than large heap
        if len(self.small_heap) > len(self.large_heap) + 1:
            val = -1 * heapq.heappop(self.small_heap)
            heapq.heappush(self.large_heap, val)

        # check: large heap is not too bigger than small heap which can happen
        if len(self.small_heap) + 1 < len(self.large_heap):
            val = heapq.heappop(self.large_heap)
            heapq.heappush(self.small_heap, -1 * val)

    def findMedian(self) -> float:
        # case 1: odd number of elements
        if len(self.small_heap) > len(self.large_heap):
            return -1 * self.small_heap[0]
        if len(self.small_heap) < len(self.large_heap):
            return self.large_heap[0]
        
        # case2: even number of elements
        return (-1 * self.small_heap[0] + self.large_heap[0]) / 2

        
        