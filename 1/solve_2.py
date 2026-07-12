from collections import defaultdict
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        nums_map = defaultdict(int)
        for idx, val in enumerate(nums):
            nums_map[val] = idx

        for idx, val in enumerate(nums):
            sub_target = target - val
            if sub_target in nums_map and idx != nums_map[sub_target]:
                return [idx, nums_map[sub_target]]

        return []
