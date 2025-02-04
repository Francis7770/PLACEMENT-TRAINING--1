class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        longest_subarr = 0
        sum = 0
        diff_index = {}

        for i, n in enumerate(nums):
            if n == 1:
                sum += 1
            else:
                sum -= 1
            
            if sum == 0:
                longest_subarr = max(longest_subarr, i+1)
            elif sum in diff_index:
                longest_subarr = max(longest_subarr, i-diff_index[sum])
            else:
                diff_index[sum] = i
        
        return longest_subarr



        
