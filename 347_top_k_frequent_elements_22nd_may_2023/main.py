from heapq import heappop, heappush, heapify
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # heap =  []
        # heapify(heap)
        # temp = defaultdict(int)
        # for i in nums: 
        #     temp[i] +=1
        
        # for i in temp: 
        #     print(temp[i])
        # temp_lst = sorted(temp.items(), key= lambda x:x[1], reverse=True)
        
        # ans = []
        # for x in range(k): 
        #     ans.append(temp_lst[x][0])
        # print(ans)

        count = {}
        freq = [[] for i in range(len(nums)+1)]

        for i in nums: 
            count[i] = 1 + count.get(i,0)
        
        for n,c in count.items(): 
            freq[c].append(n)
        ans = []
        for i in range(len(freq) - 1,0,-1): 
            for j in freq[i]: 
                ans.append(j)
                if len(ans) == k: return ans