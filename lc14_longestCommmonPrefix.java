class lc14_longestCommonPrefix {
    public String longestCommonPrefix(String[] strs) {
        String prefix = "";
        for (int i = 0; i < strs[0].length(); i++) {
            char c = strs[0].charAt(i);
            for (int j = 1; j < strs.length; j++) {
                if (i >= strs[j].length() || strs[j].charAt(i) != c)
                    return prefix;
            }
            prefix += c;
        }
        return prefix;
    }

    public static void main(String args[]) {
        lc14_longestCommonPrefix solution = new lc14_longestCommonPrefix();
        System.out.printf("Case 1: %b\n", solution.longestCommonPrefix(new String[]{"flower","flow","flight"}).equals("fl"));
        System.out.printf("Case 2: %b\n", solution.longestCommonPrefix(new String[]{"dog","racecar","car"}).equals(""));
    }
}