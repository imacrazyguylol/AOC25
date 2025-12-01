import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;

class day1_1 {
    public static void main(String[] args) throws Exception {
        BufferedReader read = new BufferedReader(new FileReader(new File("input1")));

        int count = 0;
        int pointer = 50;
        String line;
        while ((line = read.readLine()) != null) {
            boolean neg = line.contains("L");
            int amt = Integer.parseInt(line.substring(1));
            int sign = (neg ? -1 : 1);
            
            pointer += amt * sign;
            while (pointer > 99) {
                pointer -= 100;
            }
            while (pointer < 0) {
                pointer += 100;
            }
            if (pointer == 0) {
                count++;
            }
            // System.out.println(pointer);
        }

        System.out.println(count);
        read.close();
    }
}
