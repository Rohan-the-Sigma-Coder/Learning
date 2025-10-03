import java.util.Scanner;

public class Students {
    String firstName;
    String lastName;
    public Students (String firstName, String lastName) {
        this.firstName = firstName;
        this.lastName = lastName;
    }
    public String toString() {
        return "Welcome " + firstName + " " + lastName + ". You are now a new student.";
    }
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("First Name: ");
        String firstName = scanner.nextLine();
        System.out.print("Last Name: ");
        String lastName = scanner.nextLine();
        Students student1 = new Students(firstName, lastName);
        System.out.println(student1.toString());
        scanner.close();
    }
}
