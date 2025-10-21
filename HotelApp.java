import java.util.ArrayList;
import java.util.Scanner;

public class HotelApp {
    public static void main(String[] args) {
        ArrayList<Integer> rooms = new ArrayList<>();
        System.out.println("Welcome to the Grand Hotel! How can we assist you today?");
        System.out.println("1: Book a room");
        System.out.println("2: Check in");
        System.out.println("3: Check out");
        System.out.println("4: Book a reservation");
        Scanner scanner = new Scanner(System.in);
        System.out.print("Option #: ");
        int userOption = scanner.nextInt();
        switch (userOption) {
            case 1:
                int pricePerNight = 0;
                System.out.print("Enter the type of room you want to stay in (single, double, or suite): ");
                String typeOfRoom = scanner.next();
                System.out.print("What is your full name: ");
                String guestName = scanner.next() + " " + scanner.next();

                switch (typeOfRoom) {
                    case "single":
                        pricePerNight = 80;
                            break;
                    case "double":
                        pricePerNight = 140;
                            break;
                    case "suite":
                        pricePerNight = 200;
                            break;
                }
                int roomNumber = (int)((Math.random() * 100) + 100);
                rooms.add(roomNumber);
                HotelRoom guestRoom = new HotelRoom(roomNumber, guestName, pricePerNight, true);
                System.out.println(guestRoom.toString());
            case 2:
                
                    break;
            case 3:
                
                    break;
            case 4:
                
                    break;
            default:
                System.out.println("Something went wrong");;
        }
        scanner.close();



    }
}
