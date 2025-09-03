class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l, r, = 0, len(nums) - 1
        while True:
            if l == r or l > r:
                if nums[l] == target:
                    return l
                else:
                    return -1
            m = l + ((r - l) // 2)
            print(f'l {l} r {r} m {m}')
            if nums[m] < target:
                l = m + 1
            elif nums[m] > target:
                r = m - 1
            else:
                return m

        

nums=[-1,0,3,5,9,12]
target=2

solution = Solution()
print(solution.search(nums, target))