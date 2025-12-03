import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.math.BigInteger;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class day3_2 {
    public static void main(String[] args) throws Exception {
        BufferedReader in = new BufferedReader(new FileReader(new File("input3")));
        String line;

        long total = 0;
        while((line = in.readLine()) != null) {
            char[] chars = line.toCharArray();

            Map<Character, List<Integer>> indices = new HashMap<>(); // map of each number to where it appears in the line
            for (int i = 0; i < chars.length; i++) {
                char digit = chars[i];
                List<Integer> indexList;

                if (indices.containsKey(digit)) {
                    indexList = indices.get(digit);
                } else {
                    indexList = new ArrayList<>();
                    indices.put(digit, indexList);
                }

                indexList.add(i);
            }

            char[] joltageString = new char[chars.length];
            int remainingChars = chars.length;
            int filledAmt = 0;
            int minIndex = 0;

            outer: for (char i = '9'; i >= '0'; i--) {
                if (!indices.containsKey(i))
                    continue;

                List<Integer> indexList = indices.get(i);

                if (remainingChars <= 12 - filledAmt && minIndex == 0) {
                    minIndex = findMin(indices.get(i));
                    System.out.println(minIndex);
                }

                for (int j = indexList.size() - 1; j >= minIndex; j--) {
                    int index = indexList.get(j);
                    if (filledAmt == 12) {
                        break outer;
                    } else {
                        joltageString[index] = i;                        
                        filledAmt++;
                    }
                    remainingChars--;
                }
            }

            String joltage = new String(joltageString).replaceAll("\\D","");

            System.out.println(joltage + "\n\n");

            total += Long.parseLong(joltage);
        }

        System.out.println(total);
    }

    private static int findMin(List<Integer> list) {
        if (list == null)
            return 0;

        int min = list.get(0);
        for (int i : list) {
            if (i < min)
                min = i;
        }
        return min;
    }
}
