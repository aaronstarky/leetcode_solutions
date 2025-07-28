/*
 * DONE 🎉
 * Time Complexity: O(m + n)
 * Space Complexity: O(n)
 */
import java.util.Arrays;

class lc6_ZigzagConversation {
    public String convert(String s, int numRows) {
        if (numRows == 1)
            return s;
        String[] rows = new String[numRows];
        Arrays.fill(rows, "");
        int r = 0;
        String action = "zig";
        for (char letter : s.toCharArray()) {
            rows[r] += letter;
            if (r == numRows - 1)
                action = "zag";
            if (r == 0) 
                action = "zig";
            if (action.equals("zig"))
                r++;
            else
                r--;
        }
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < rows.length; i++) {
            sb.append(rows[i]);
        }
        return sb.toString();
    }

    public static void main(String args[]) {
        lc6_ZigzagConversation solution = new lc6_ZigzagConversation();

        System.out.printf("Case 1: %b\n", solution.convert("PAYPALISHIRING", 3) == "PAHNAPLSIIGYIR");
        System.out.printf("Case 2: %b\n", solution.convert("PAYPALISHIRING", 4) == "PINALSIGYAHRPI");
        System.out.printf("Case 3: %b\n", solution.convert("A", 1) == "A");
        System.out.printf("Case 3: %b\n", solution.convert("AB", 1) == "AB");

    }
}