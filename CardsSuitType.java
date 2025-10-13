public class CardsSuitType {
    public static String type;
    public static String value;
    public CardsSuitType (String suit, String value) {
        this.type = suit;
        this.value = value;
    }
    public static String getType() {
        return type;
    }
    public static String getValue() {
        return value;
    }

    public static int add(int num1, int num2) {
            return num1 + num2;
    }
    public static void main(String[] args) {
        System.out.println(add(1, 2));
    }
}