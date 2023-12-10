class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            if nums[i] == 0:
                nums.pop(i)
                nums.insert(0,0)
        
        for i in range(-1,-len(nums)-1,-1):
            if nums[i] == 2:
                nums.pop(i)
                nums.append(2)
        return nums
