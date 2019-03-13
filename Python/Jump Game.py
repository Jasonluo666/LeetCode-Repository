class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        if not nums:
            return False
        
        # boolean map -> store the positions that can be reached
        booleanMap = [False for _ in range(len(nums))]
        booleanMap[0] = True
        index, current_max = 0, 0
        
        # walk through the boolean map -> break if get stuck
        while index < len(nums) and booleanMap[index] == True:
            jump = nums[index]

            # if there are new steps that can be reached -> update the new map
            if current_max < jump:
                for hop in range(current_max + 1, jump + 1):
                    if index + hop < len(nums):
                        booleanMap[index + hop] = True
                current_max = jump
            
            # move forward, decrease current_max cuz we have moved one step
            index += 1
            current_max -= 1
        
        if index == len(nums):
            return True
        else:
            return False
        