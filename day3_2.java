import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class day3_2 {
    public static void main(String[] args) throws Exception {
        BufferedReader in = new BufferedReader(new FileReader(new File("input3")));
        String line;
        int lineNumber = 1;

        System.out.println("\n\n\n");

        long total = 0;
        while ((line = in.readLine()) != null) {
            char[] chars = line.toCharArray();

            Map<Character, ArrayList<Integer>> indices = new HashMap<>(); // map of each number to where it appears in
                                                                          // the
            // line
            for (int i = 0; i < chars.length; i++) {
                char digit = chars[i];
                ArrayList<Integer> indexList;

                if (indices.containsKey(digit)) {
                    indexList = indices.get(digit);
                } else {
                    indexList = new ArrayList<>();
                    indices.put(digit, indexList);
                }

                indexList.add(i);
            }

            char[] joltageString = new char[chars.length];
            int filledAmt = 0;
            int minIndex = 0;
            int rightMostFreeIndex = chars.length - 1;

            outer: for (char i = '9'; i >= '0'; i--) {
                if (!indices.containsKey(i))
                    continue;

                ArrayList<Integer> indexList = indices.get(i); // always in order
                // Collections.reverse(indexList);

                for (int index : indexList) {
                    if (filledAmt == 12) {
                        break outer;
                    }

                    if (index < minIndex)
                        continue;

                    if (rightMostFreeIndex - index >= 12 - filledAmt) {
                        minIndex = index;
                    } else {
                        while (rightMostFreeIndex >= index) {
                            joltageString[rightMostFreeIndex] = chars[rightMostFreeIndex];
                            rightMostFreeIndex--;
                            filledAmt++;
                            if (filledAmt == 12)
                                break outer;
                        }
                        filledAmt--; // account for adding 1 extra when rmfi = index
                    }

                    joltageString[index] = i;

                    while (joltageString[rightMostFreeIndex] != '\u0000') {
                        rightMostFreeIndex--;
                    }

                    filledAmt++;
                }
            }

            String joltage = new String(joltageString).replaceAll("\\D", "");

            System.out.println(lineNumber);
            System.out.println(joltage + "\n\n");

            total += Long.parseLong(joltage);
            lineNumber++;
        }

        System.out.println(total);
    }
}
