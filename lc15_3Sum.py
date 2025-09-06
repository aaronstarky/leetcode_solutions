def threeSum(nums):
    nums.sort()
    result = []
    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        j = i + 1
        k = len(nums) - 1
        while j < k:
            total = nums[i] + nums[j] + nums[k]
            if total > 0:
                k -= 1
            elif total < 0:
                j += 1
            else:
                result.append([nums[i], nums[j], nums[k]])
                j += 1
                while nums[j] == nums[j-1] and j < k:
                    j += 1
    return result


def threeSum2(nums: list[int]) -> list[list[int]]:
    nums.sort()
    result = []
    l, r = 0, len(nums)-1
    while l < r - 1:
        if l > 0 and nums[l] == nums[l - 1]:
            l += 1
            continue
        if r < len(nums) - 1 and nums[r] == nums[r + 1]:
            r -= 1
            continue
        print(f'l {l} r {r}')
        mid_sum = nums[l] + nums[r]
        # if the last part is between the two, find it
        if nums[l] <= mid_sum <= nums[r]:
            l_bound = l
            r_bound = r
            m = l + ((r-l) // 2)
            while l_bound < r_bound:
                if l_bound == r_bound or l_bound == r_bound - 1:
                    break
                if nums[m] == mid_sum:
                    append = [nums[l], nums[m],nums[r]]
                    print(f'appending {append}')
                    result.append([nums[l], nums[m],nums[r]])
                elif nums[m] < mid_sum:
                    l_bound = m + 1
                else:
                    r_bound = m - 1
        else:
            print('hitting not match territory')
            if mid_sum <= nums[l]:
                r -= 1
            if mid_sum >= nums[r]:
                l += 1
                    

case1 = [-1,0,1,2,-1,-4]
print(threeSum(case1))

print(threeSum2(case1))