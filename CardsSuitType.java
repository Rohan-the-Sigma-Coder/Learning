public class CardsSuitType {
    public static String type;
    public static String value;
    public CardsSuitType (String suit, String value) {
        this.type = suit;
        this.value = value;
    }
    public static String type() {
        return type;
    }
    public static String value() {
        return value;
    }
}

