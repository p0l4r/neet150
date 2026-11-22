class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        i = 0 # first pointer starting from first value of nums
        j = len(nums) # length of given array
        k = 0 # counter of occurance and also works as a pointer to next available position

        while i < j:
            
            if nums[i] != val: # if val doesn't occur
                nums[k] = nums[i] # copy it in k position
                k = k + 1 # increase k (only when val doesn't occur)

            i = i + 1 # keep moving i , if val doesn't occur i and k moves together
            # if val occurs i moves alone. So we skip the occurence while rebuilding the array
        
        return k
        