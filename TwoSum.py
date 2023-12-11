class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        p_low = 0
        p_high = len(numbers)-1
        
        while numbers[p_low] + numbers[p_high] != target:
            if numbers[p_low] + numbers[p_high] < target:
                p_low += 1
            else:
                p_high -= 1
        return [p_low + 1 , p_high + 1]

