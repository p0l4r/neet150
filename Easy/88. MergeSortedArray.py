class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m - 1 # pointer for nums1 indicating last number in nums1
        j = n - 1 # pointer for nums2 indicating last number in nums2
        k = m + n -1 # pointer for nums1 indicating last available free space in nums1

        while i>=0 and j>=0: # in some edge case when nums1=[0], m = 0, nums2=[1], n = 1, i will become -1
            if nums1[i] <= nums2[j]:
                nums1[k] = nums2[j]
                j = j - 1
            else:
                nums1[k] = nums1[i]
                i = i - 1
            
            k = k - 1
        
        while j>=0: # this is to counter the edge case where i becomes -1
            nums1[k] = nums2[j]
            k = k - 1
            j = j - 1
             
        