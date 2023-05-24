class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        total = res = 0 
        heap = []
        pair = zip(nums1,nums2)
        sorted_pair = sorted(pair, key = lambda x: -x[1])
        for x in sorted_pair: 
            num1, num2 = x
            heappush(heap,num1)
            total+=num1
            if len(heap)>k: 
                total-=heappop(heap)
            if len(heap) == k: 
                res = max(res,total*num2)
        return res