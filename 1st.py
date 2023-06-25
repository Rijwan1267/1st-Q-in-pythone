def moveZeroes(nums):
    """
    Moves all zeros to the end of the given array while maintaining the relative order of non-zero elements.
    """
   
    nonzero_pos = 0
    
    for i in range(len(nums)):

        if nums[i] != 0:
           
            nums[i], nums[nonzero_pos] = nums[nonzero_pos], nums[i]
            
            nonzero_pos += 1


nums1 = [0, 1, 0, 3, 12]
moveZeroes(nums1)
print(nums1)  

nums2 = [0]
moveZeroes(nums2)
print(nums2)  
