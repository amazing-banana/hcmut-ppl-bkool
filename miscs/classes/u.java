@SuppressWarnings("unused")
public class u {
    public static float i2f(int e) {
        return e;
    }

    public static boolean i2b(int e) {
        return e != 0;
    }
    
    public static String i2str(int e) {
        return String.valueOf(e);
    }
    
    public static int f2i(float e) {
        return (int) e;
    }
    
    public static boolean f2b(float e) {
        return Float.compare(e, 0) == 0;
    }
    
    public static String f2str(float e) {
        return String.valueOf(e);
    }
    
    public static int b2i(boolean e) {
        return e ? 1 : 0;
    }
    
    public static float b2f(boolean e) {
        return e ? 1.0f : 0.0f;
    }
    
    public static String b2str(boolean e) {
        return String.valueOf(e);
    }
    
    public static int str2i(String e) {
        return Integer.parseInt(e);
    }
    
    public static float str2f(String e) {
        return Float.parseFloat(e);
    }
    
    public static boolean str2b(String e) {
        return Boolean.parseBoolean(e);
    }
    
    public static int strlen(String e) {
        if (e == null) return -1;
        else return e.length();
    }
    
    public static int arrlen(Object e) {
        if (e instanceof Object[]) return ((Object[]) e).length;
        else return -1;
    }

    public static void printRef(Object e) {
        System.out.println(e);
    }
    
    public static boolean strCmp(String a, String b) {
        if (a == null) return b == null;
        else return a.equals(b);
    }
    
    public static boolean floatCmp(float a, float b) {
        return Float.compare(a, b) == 0;
    }

    
    public static boolean isNotNull(Object a) {
        return a != null;
    }
    
    public static boolean isNull(Object a) {
        return a == null;
    }

    public static void printLn() {
        System.out.println();
    }
}
