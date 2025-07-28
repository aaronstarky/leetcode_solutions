// DONE SOLO

/*
There is an integer array nums sorted in non-decreasing order (not necessarily with distinct values).

Before being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,4,4,5,6,6,7] might be rotated at pivot index 5 and become [4,5,6,6,7,0,1,2,4,4].

Given the array nums after the rotation and an integer target, return true if target is in nums, or false if it is not in nums.

You must decrease the overall operation steps as much as possible.
 */
import java.util.LinkedList;
import java.util.Queue;

public class lc84 {
    public boolean search(int[] nums, int target) {
        if (nums.length == 0)
            return false;
        if (nums.length == 1) {
            if (nums[0] == target)
                return true;
            return false;
        }
        Queue<int[]> queue = new LinkedList<>();
        int[] initialTuple = {0, nums.length - 1};
        queue.add(initialTuple);
        while (!queue.isEmpty()) {
            int[] tuple = queue.remove();
            int left = tuple[0];
            int right = tuple[1];
            int mid = left + (right - left) / 2;
            if (target == nums[mid] || target == nums[left] || target == nums[right]) return true;
            if (right - left <= 1) continue;
            if (nums[left] < nums[mid]) {
                if (nums[left] < target && target <= nums[mid]) {
                    right = mid - 1;
                } else {
                    left = mid + 1;
                }
                int[] newTuple = {left, right};
                queue.add(newTuple);
            } else if (nums[mid] < nums[right]) {
                if (nums[mid] < target && target <= nums[right]) {
                    left = mid + 1;
                } else {
                    right = mid - 1;
                }
                int[] newTuple = {left, right};
                queue.add(newTuple);
            } else {
                int[] newTuple1 = {left, mid-1};
                int[] newTuple2 = {mid+1, right};
                queue.add(newTuple1);
                queue.add(newTuple2);
            }
        }
        return false;
    }

    public static void main(String[] args) {
        lc84 solution = new lc84();
        int[] nums1 = { 2, 5, 6, 0, 0, 1, 2 };
        int[] nums2 = { 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1 };
        System.out.printf("Case 1: %b\n", (solution.search(nums1, 0) == true));
        System.out.printf("Case 2: %b\n", (solution.search(nums1, 3) == false));
        System.out.printf("Case 3: %b\n", (solution.search(nums2, 2) == true));
    }
}
