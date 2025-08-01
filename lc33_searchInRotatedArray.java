public class lc33_searchInRotatedArray {
    public int search(int[] nums, int target) {
        int left = 0;
        int right = nums.length - 1;
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (nums[mid] == target)
                return mid;
            if (nums[left] <= nums[mid]) {
                if (nums[left] <= target && target < nums[mid]) {
                    right = mid - 1;
                } else {
                    left = mid + 1;
                }
            } else {
                if (nums[mid] < target && target <= nums[right]) {
                    left = mid + 1;
                } else {
                    right = mid - 1;
                }
            }
        }
        return -1;
    }

    public static void main(String args[]) {
        lc33_searchInRotatedArray solution = new lc33_searchInRotatedArray();
        int[] nums1 = { 4, 5, 6, 7, 0, 1, 2 };
        int[] nums2 = { 1 };
        System.out.printf("Case 1: %b\n", (solution.search(nums1, 0) == 4));
        System.out.printf("Case 2: %b\n", (solution.search(nums1, 3) == -1));
        System.out.printf("Case 3: %b\n", (solution.search(nums2, 0) == -1));
    }
}
