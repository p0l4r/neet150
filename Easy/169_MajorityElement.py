class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        candidate = -1 # boyer-moore majority voting algo 
        vote = 0 
        count = 0 

        for i in range(0,len(nums)):
            if vote==0:
                candidate = nums[i]
                vote = 1
            else:
                if candidate == nums[i]:
                    vote = vote + 1
                else:
                    vote = vote - 1
        
        return candidate

        