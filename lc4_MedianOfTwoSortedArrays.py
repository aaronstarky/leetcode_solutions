# DONE
class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        i1, i2 = 0, 0
        while True:
            if i1 >= len(nums1):
                nums1 = nums1 + nums2[i2:]
                break
            if i2 >= len(nums2):
                break
            if nums1[i1] < nums2[i2]:
                i1 += 1
            else:
                nums1 = nums1[:i1] + [nums2[i2]] + nums1[i1:]
                i2 += 1
        median = 0
        # If total length is even, divide sum of two middle elements by two
        if (len(nums1) + len(nums2)) % 2 == 0:
            median = (nums1[(len(nums1)//2) - 1] + nums1[len(nums1)//2]) / 2
        # If not even, retrieve middle element
        else:
            median = nums1[len(nums1)//2]
        return median
    
solution = Solution()

print(f"Case 1: {solution.findMedianSortedArrays([1,3], [2]) == 2}")
print(f"Case 2: {solution.findMedianSortedArrays([1,2], [3,4]) == 2.5 }")
