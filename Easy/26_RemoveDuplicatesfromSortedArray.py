class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        k = 1 # points towards next available unique value

        for i in range(1,len(nums)):
            if nums[i] != nums[k-1]:
                nums[k] = nums[i]
                k = k + 1
        
        return k