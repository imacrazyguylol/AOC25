import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;

public class day2_1 {
    public static void main(String[] args) throws Exception {
        BufferedReader in = new BufferedReader(new FileReader(new File("input2")));

        String line = in.readLine();
        String[] tokens = line.split(",");
        Range[] ranges = new Range[tokens.length];
        for (int i = 0; i < tokens.length; i++) {
            ranges[i] = new Range(tokens[i]);
        }

        long total = 0;
        for (Range r : ranges) {
            total += r.countValIDs();
        }
        System.out.println(total);

        in.close();
    }   
}

class Range {
    public long min;
    public long max;
    
    public Range(long min, long max) {
        this.min = min;
        this.max = max;
    }

    public Range(String in) {
        String[] nums = in.split("-");
        this.min = Long.parseLong(nums[0]);
        this.max = Long.parseLong(nums[1]);

        if (nums[0].length() % 2 == 1) {
            this.min = (long) Math.pow(10, nums[0].length());
        }
    }

    public long countValIDs() {
        long count = 0;
        for (long i = min; i <= max; i++) {
            String s = "" + i;
            int len = s.length();

            if (len % 2 == 1)
                i = (long) Math.pow(10, len);

            int half = len / 2;
            
            if (s.substring(0, half).equals(s.substring(half))) {
                count += i;
            }
        }
        return count;
    }
}
