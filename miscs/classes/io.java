import java.io.*;
import java.io.IOException;
import java.util.Arrays;


public class io {
    public final static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    public final static Writer writer = new BufferedWriter(new OutputStreamWriter(System.out));


    /**
     * reads and returns an integer value from the standard input
     *
     * @return int an integer number read from standard input
     */
    public static int readInt() {
        try {
            return Integer.parseInt(input.readLine());
        } catch (IOException e) {
            throw new RuntimeException(Arrays.toString(e.getStackTrace()));
        }
    }


    /**
     * print out the value of the integer i to the standard output
     *
     * @param i the value is printed out
     */
    public static void writeInt(int i) {
        System.out.print(i + "");
    }

    /**
     * same as putInt except that it also prints a newline
     *
     * @param i the value is printed out
     */
    public static void writeIntLn(int i) {
        System.out.println(i + "");
    }

    /**
     * return a floating-point value read from the standard input
     *
     * @return float the floating-point value
     */
    public static float readFloat() {
        try {
            return Float.parseFloat(input.readLine());
        } catch (IOException e) {
            throw new RuntimeException(Arrays.toString(e.getStackTrace()));
        }
    }

    /**
     * print out the value of the float f to the standard output
     *
     * @param f the floating-point value is printed out
     */
    public static void writeFloat(float f) {
        System.out.print(f + "");
    }

    /**
     * same as putFloat except that it also prints a newline
     *
     * @param f the floating-point value is printed out
     */
    public static void writeFloatLn(float f) {
        System.out.println(f + "");
    }

    /**
     * reads and returns a boolean value from the standard input
     *
     * @return int a boolean value read from standard input
     */
    public static boolean readBool() {
        try {
            String str = input.readLine();
            if (str.equalsIgnoreCase("true")) return true;
            else if (str.equalsIgnoreCase("false")) return false;
            else throw new RuntimeException(str + " is not a boolean");
        } catch (IOException e) {
            throw new RuntimeException(Arrays.toString(e.getStackTrace()));
        }
    }

    /**
     * print out the value of the boolean b to the standard output
     *
     * @param b the boolean value is printed out
     */
    public static void writeBool(boolean b) {
        System.out.print(b);
    }

    /**
     * same as putBoolLn except that it also prints a new line
     *
     * @param b the boolean value is printed out
     */
    public static void writeBoolLn(boolean b) {
        System.out.println(b);
    }


    /**
     * Read string
     */
    public static String readStr() {
        try {
            return input.readLine();
        } catch (IOException e) {
            throw new RuntimeException(Arrays.toString(e.getStackTrace()));
        }
    }

    /**
     * same as putString except that it also prints a new line
     *
     * @param a the string is printed out
     */
    public static void writeStr(String a) {
        System.out.print(a);
    }

    /**
     * print out an empty line
     **/
    public static void writeStrLn(String a) {
        System.out.println(a);
    }

    public static void close() {
        try {
            writer.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}

