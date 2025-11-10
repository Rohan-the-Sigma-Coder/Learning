import java.time.LocalDate;
import java.time.format.DateTimeFormatter;
import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class HotelApp {

    // Stores ALL reservations by reservation ID
    public static Map<Integer, HotelReservations> allReservations = new HashMap<>();

    public static Scanner scanner = new Scanner(System.in);
    public static Integer userOption;

    public static void showInterface() {
        System.out.println("\nWelcome to the Grand Hotel!");
        System.out.println("1: Book a reservation");
        System.out.println("2: Check in");
        System.out.println("3: Check out");
        System.out.println("4: Exit");
        System.out.print("Option #: ");
        userOption = scanner.nextInt();
        scanner.nextLine(); // clear buffer
    }

    public static void main(String[] args) {

        while (true) {
            showInterface();

            switch (userOption) {

                case 1:  // BOOK RESERVATION
                    bookReservation();
                    break;

                case 2:  // CHECK IN
                    checkIn();
                    break;

                case 3:  // CHECK OUT
                    checkOut();
                    break;

                case 4:  // EXIT
                    System.out.println("Goodbye!");
                    scanner.close();
                    System.exit(0);

                default:
                    System.out.println("Invalid option. Try again.");
            }
        }
    }


    // ------------------------
    //       FUNCTIONS
    // ------------------------

    public static void bookReservation() {
        int pricePerNight = 0;

        System.out.print("Enter room type (single, double, suite): ");
        String typeOfRoom = scanner.nextLine().trim().toLowerCase();

        System.out.print("What is your full name: ");
        String guestName = scanner.nextLine().trim();

        System.out.print("When is check-in? (dd/MM/yyyy): ");
        LocalDate checkInDate = LocalDate.parse(scanner.nextLine().trim(),
                DateTimeFormatter.ofPattern("dd/MM/yyyy"));

        System.out.print("When is check-out? (dd/MM/yyyy): ");
        LocalDate checkOutDate = LocalDate.parse(scanner.nextLine().trim(),
                DateTimeFormatter.ofPattern("dd/MM/yyyy"));

        switch (typeOfRoom) {
            case "single": pricePerNight = 80; break;
            case "double": pricePerNight = 140; break;
            case "suite":  pricePerNight = 200; break;
            default:
                System.out.println("Invalid room type. Reservation cancelled.");
                return;
        }

        int roomNumber = (int)((Math.random() * 100) + 100);
        int reservationID = (int)(Math.random() * 9000 + 1000); // 4-digit ID

        HotelRoom guestRoom = new HotelRoom(roomNumber, guestName, pricePerNight, true);
        HotelReservations reservation =
                new HotelReservations(reservationID, checkInDate, checkOutDate, roomNumber);

        // Store reservation
        allReservations.put(reservationID, reservation);

        System.out.println("\n✅ Reservation Created!");
        System.out.println(guestRoom);
        System.out.println(reservation);
    }


    public static void checkIn() {
        System.out.print("Enter your reservation ID: ");
        int reservationId = scanner.nextInt();
        scanner.nextLine();

        HotelReservations res = allReservations.get(reservationId);

        if (res == null) {
            System.out.println("❌ Reservation not found.");
            return;
        }

        if (res.isCheckedIn) {
            System.out.println("❗ You are already checked in.");
            return;
        }

        res.isCheckedIn = true;
        System.out.println("✅ Successfully checked in!");
    }


    public static void checkOut() {
        System.out.print("Enter your reservation ID: ");
        int reservationId = scanner.nextInt();
        scanner.nextLine();

        HotelReservations res = allReservations.get(reservationId);

        if (res == null) {
            System.out.println("❌ Reservation not found.");
            return;
        }

        if (!res.isCheckedIn) {
            System.out.println("❗ You must check in before checking out.");
            return;
        }

        allReservations.remove(reservationId);
        System.out.println("✅ Successfully checked out!");
    }
}
