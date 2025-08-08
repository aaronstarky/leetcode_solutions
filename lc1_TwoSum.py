class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diffs = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diffs.get(diff) is not None:
                return [diffs.get(diff), i] if diffs.get(diff) < i else [i, diffs.get(diff)]
            diffs[nums[i]] = i