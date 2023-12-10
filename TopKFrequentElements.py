import heapq as hq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        dic_cnt = {}

        for num in nums:
            if num in dic_cnt.keys():
                dic_cnt[num] += 1
            else:
                dic_cnt[num] = 1

        
        n = len (nums)
        lst_cnt = []

        for i in range (n+1):
          lst_cnt.append([])

        for key, value in dic_cnt.items():
            lst_cnt[value].append(key)

        res=[]
        
      
        for i in [-x for x in range(1,n+1)]:
            while k > 0 and lst_cnt[i]:
                res.append(lst_cnt[i][0])
                lst_cnt[i].pop(0)
                k-=1
        return res
