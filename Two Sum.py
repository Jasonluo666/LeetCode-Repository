class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        # create hash table
        num_hash = {}
        for index in range(len(nums)):
            if nums[index] in num_hash.keys():
                num_hash[nums[index]].append(index)
            else:
                num_hash[nums[index]] = [index]
        
        # for each unique element, find the pair in the hash table
        for num in num_hash.keys():
            other_num = target - num
            if other_num in num_hash.keys():
                if num != other_num:
                    pair_list = (sorted([num_hash[num][0], num_hash[other_num][0]]))
                    break
                elif len(num_hash[num]) > 1:
                    pair_list = ([num_hash[num][0], num_hash[other_num][1]])
                    break
        
        return pair_list
        