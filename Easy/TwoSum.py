# Ekdatha Arramreddy

def twoSum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        """
    
        targets = {}
        for i in range(len(nums)):
            if target - nums[i] in targets:
                return [targets[target - nums[i]], i]
            targets[nums[i]] = i
        return[]