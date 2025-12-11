import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.LinkedList;
import java.util.List;
import java.util.Set;

class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader in = new BufferedReader(new FileReader(new File("input10")));
        String line;

        int presses = 0;
        while ((line = in.readLine()) != null) {
            String[] tokens = line.split(" ");

            BitState goal = new BitState(tokens[0]);
            int length = goal.length;

            List<BitState> dirs = new ArrayList<BitState>();

            for (int i = 1; i < tokens.length - 1; i++) {
                dirs.add(new BitState(tokens[i], length));
            }

            Set<BitState> visited = new HashSet<>();
            List<BitState> path = explore(new BitState(0, length), dirs, goal, visited);
            int minPresses = path.size();
            presses += minPresses;
            System.out.println(minPresses);
        }

        System.out.println(presses);

        in.close();
    }

    // TODO: make bfs lmao
    public static List<BitState> explore(BitState pos, List<BitState> directions, BitState goal, Set<BitState> visited) {
        int posDistFromGoal = pos.dist(goal);
        visited.add(pos);
        for (BitState dir : directions) {
            BitState nextPos = pos.xor(dir);
            if (nextPos.equals(goal)) {
                List<BitState> path = new LinkedList<BitState>();
                path.add(dir);
                return path;
            }

            if (nextPos.dist(goal) > posDistFromGoal || visited.contains(nextPos))
                continue;

            List<BitState> path = explore(nextPos, directions, goal, visited);
            if (path != null) {
                path.add(0, dir);
                return path;
            }
        }
        return null;
    }
}

class BitState {
    int bits;
    final int length;
    
    /**
     * @param bits = the bit representation of the machine state OR button
     * @param length = the maximum length of the bit string AKA the length of the machine's light diagram
     * @implNote the 0 place in the bitstring => the 0th indicator light
     */
    public BitState(int bits, int length) {
        this.bits = bits;
        this.length = length;
    }

    // for parsing the indicator lights
    public BitState(String indicator) {
        char[] chars = indicator.substring(1, indicator.length() - 1).toCharArray();
        this.length = chars.length;

        this.bits = 0;
        for (int i = 0; i < this.length; i++) {
            if (chars[i] == '#')
                this.bits |= (1 << i);
        }
    }

    // for parsing the buttons
    public BitState(String buttonlights, int length) {
        String[] places = buttonlights.substring(1, buttonlights.length() - 1).split(",");
        this.length = length;
        this.bits = 0;

        for (String s : places) {
            int i = Integer.parseInt(s);
            this.bits |= (1 << i);
        }
    }

    public BitState xor(BitState other) {
        return new BitState(this.bits ^ other.bits, this.length);
    }

    /**
     * @param goal
     * @return The number of different bits between this and goal. 
     * The distance in n-dimensional space (n being the bit length) is sqrt of this number.
     * @throws Exception If the bitstrings are not of the same length -- this shouldn't happen on the same line.
     */
    public int dist(BitState goal) {
        if (this.length != goal.length)
            return -1;

        BitState xored = this.xor(goal);
        return Integer.bitCount(xored.bits);
    }

    public boolean equals(BitState other) {
        return this.bits == other.bits;
    }

    @Override
    public int hashCode() {
        return this.bits;
    }
}