class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k 
        self.heap = []

        for num in nums: 
            self.add(num)
        
    def add(self, val: int) -> int:
        heapq.heappush(self.heap,val)
        if len(self.heap)>self.k: 
            heapq.heappop(self.heap)
        return self.heap[0]
        # self.nums.append(val)
        # self.nums = sorted(self.nums)
        # return self.nums[-self.k]
        