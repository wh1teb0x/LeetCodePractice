class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        nums_map: dict[int] = dict()
        for idx, val in enumerate(nums):
            nums_map[val] = idx

        for idx, val in enumerate(nums):
            sub_target = target - val
            sub_idx = nums_map.get(sub_target)
            if not sub_idx and idx != sub_idx:
                return [idx, nums_map[sub_target]]
            
        return []
