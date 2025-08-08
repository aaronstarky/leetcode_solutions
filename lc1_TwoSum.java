import java.util.HashMap;

class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> diffs = new HashMap<>();
        int result[] = new int[0];
        for (int i = 0; i < nums.length; i++) {
            int diff = target - nums[i];
            if (diffs.get(diff) != null) {
                if (diffs.get(diff) < i) {
                    result = new int[] {diffs.get(diff), i};
                } else {
                    result = new int[] {diffs.get(diff), i};
                }
            }
            diffs.put(nums[i], i);
        }
        return result;
    }
}