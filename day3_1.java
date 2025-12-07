import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;

public class day3_1 {
    public static void main(String[] args) throws Exception {
        BufferedReader in = new BufferedReader(new FileReader(new File("input3")));
        String line;

        int total = 0;
        while((line = in.readLine()) != null) {
            char[] chars = line.toCharArray();
            int tensIndex = 0;
            for (int i = 1; i < chars.length - 1; i++) {
                if (chars[i] > chars[tensIndex]) {
                    tensIndex = i;
                    System.out.println(line + " - tens\n" + " ".repeat(tensIndex) + "^");
                }
            }

            int onesIndex = tensIndex + 1;
            for (int i = tensIndex + 2; i < chars.length; i++) {
                if (chars[i] > chars[onesIndex]) {
                    onesIndex = i;
                    System.out.println(line + " - ones\n" + " ".repeat(onesIndex) + "^");
                }
            }

            int joltage = ((chars[tensIndex] - '0') * 10) + (chars[onesIndex] - '0');
            total += joltage;
            System.out.println(joltage + "\n\n");
        }

        System.out.println(total);

        in.close();
    }
}
