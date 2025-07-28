// DONE SOLO

/*
Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of this array.

You must write an algorithm that runs in O(log n) time.
 */

public class lc153 {
    public int findMin(int[] nums) {
        double smallest = Double.POSITIVE_INFINITY;
        int left = 0, right = nums.length - 1;
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (nums[mid] < nums[right]) {
                if (nums[mid] < smallest) {
                    smallest = nums[mid];
                }
                right = mid - 1;
            } else {
                if (nums[right] < smallest) {
                    smallest = nums[mid];
                }
                left = mid + 1;
            }
        }
        return (int) smallest;
    }

    public static void main(String[] args) {
        lc153 solution = new lc153();
        int[] nums1 = {3,4,5,1,2};
        int[] nums2 = {4,5,6,7,0,1,2};
        int[] nums3 = {11,13,15,17};
        int expected1 = 1;
        int expected2 = 0;
        int expected3 = 11;
        System.out.printf("Case 1: %d %b\n", solution.findMin(nums1), (solution.findMin(nums1) == expected1));
        System.out.printf("Case 2: %d %b\n", solution.findMin(nums2), (solution.findMin(nums2) == expected2));
        System.out.printf("Case 3: %d %b\n", solution.findMin(nums3), (solution.findMin(nums3) == expected3));

    }
}