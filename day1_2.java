import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;

class day1_2 {
    public static void main(String[] args) throws Exception {
        BufferedReader read = new BufferedReader(new FileReader(new File("input1")));

        int count = 0;
        int pointer = 50;
        String line;
        while ((line = read.readLine()) != null) {
            int sign = (line.contains("L") ? -1 : 1);
            int amt = Integer.parseInt(line.substring(1));
            System.out.println(pointer + " " + sign * amt);
            while (amt > 99) {
                amt -= 100;
                count++;
                System.out.println("  " + sign * amt);
            }

            if (amt != 0) {
                if (pointer != 0) {
                    pointer += amt * sign;
                    if (pointer > 99 || pointer < 0) {
                        pointer -= 100 * sign;
                        count++;
                        System.out.println("  " + sign * amt);
                    } else if (pointer == 0) {
                        count++;
                        System.out.println("  " + sign * amt);
                    }
                } else {
                    pointer += amt * sign;
                    if (pointer > 99 || pointer < 0) {
                        pointer -= 100 * sign;
                    }
                }
            }
            
            // System.out.println(pointer);
            // System.out.println();
        }

        System.out.println(count);
        read.close();
    }
}
