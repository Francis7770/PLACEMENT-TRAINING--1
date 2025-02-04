class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.num_idx_dict = {}

        for index, num in enumerate(nums):
            if num not in self.num_idx_dict:
                self.num_idx_dict[num] = deque([])
            self.num_idx_dict[num].append(index)
        
        return

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """

        pop = self.num_idx_dict[target].popleft()
        self.num_idx_dict[target].append(pop)

        
        return pop
