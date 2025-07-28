/*
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.
 */

class lc34 {
    public int[] searchRange(int[] nums, int target) {
        int[] result = { -1, -1 };
        if (nums.length == 0)
            return result;
        result[0] = this.binarySearch(nums, target, true);
        result[1] = this.binarySearch(nums, target, false);
        return result;
    }

    public int binarySearch(int[] nums, int target, boolean findFirst) {
        int left = 0;
        int right = nums.length - 1;
        int location = -1;
        while (left <= right) {
            int mid = left + ((right - left) / 2);
            if (target > nums[mid]) {
                left = mid + 1;
            } else if (target < nums[mid]) {
                right = mid - 1;
            } else {
                location = mid;
                if (findFirst) {
                    right = mid - 1;
                } else {
                    left = mid + 1;
                }
            }
        }
        return location;
    }

    public static void main(String[] args) {
        lc34 solution = new lc34();

        int[] nums1 = { 5, 7, 7, 8, 8, 10 };
        int[] nums2 = {};

        int[] result1 = { 3, 4 };
        int[] result2 = { -1, -1 };
        int[] result3 = { -1, -1 };
        int[] expected1 = solution.searchRange(nums1, 8);
        int[] expected2 = solution.searchRange(nums1, 6);
        int[] expected3 = solution.searchRange(nums2, 0);

        System.out.printf("Case 1: {%d, %d} %b\n", expected1[0], expected1[1], (expected1[0] == result1[0] && expected1[1] == result1[1]));
        System.out.printf("Case 2: {%d, %d} %b\n", expected2[0], expected2[1], (expected2[0] == result2[0] && expected2[1] == result2[1]));
        System.out.printf("Case 3: {%d, %d} %b\n", expected3[0], expected3[1], (expected3[0] == result3[0] && expected3[1] == result3[1]));
    }
}
