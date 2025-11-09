import java.time.LocalDate;
import java.time.format.DateTimeFormatter;
import java.util.ArrayList;
import java.util.Scanner;

public class HotelApp {
    public static HotelReservations reservation;
    public static void main(String[] args) {
        ArrayList<Integer> occupiedRooms = new ArrayList<>();
        ArrayList<Integer> reservations = new ArrayList<>();
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
                scanner.nextLine();
                System.out.print("When will you check in (dd/MM/yyyy): ");
                String dateString = scanner.nextLine();
                DateTimeFormatter formatter = DateTimeFormatter.ofPattern("dd/MM/yyyy");
                LocalDate checkInDate = LocalDate.parse(dateString, formatter);
                System.out.print("When will you check out (dd/MM/yyyy: ");
                String dateString1 = scanner.nextLine();
                DateTimeFormatter formatter1 = DateTimeFormatter.ofPattern("dd/MM/yyyy");
                LocalDate checkOutDate = LocalDate.parse(dateString1, formatter1);
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
                int reservationID = (int)(Math.random() * 100);
                occupiedRooms.add(roomNumber);
                reservations.add(reservationID);
                HotelRoom guestRoom = new HotelRoom(roomNumber, guestName, pricePerNight, true);
                reservation = new HotelReservations(reservationID, checkInDate, checkOutDate, roomNumber);
                System.out.println(guestRoom.toString());
                System.out.println(reservation.toString());
            case 2:
                System.out.print("What is your reservation Id?: ");
                Integer reservationId = scanner.nextInt();
                boolean isReserved = reservations.contains(reservationId);
                if (isReserved == true) {
                    reservation.isCheckedIn = true;
                }
                
                    break;
            case 3:
                
                    break;
            case 4:
                
                    break;
            default:
                System.out.println("Please enter a valid number");;
        }
        scanner.close();



    }
}
