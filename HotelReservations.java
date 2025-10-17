import java.time.LocalDate;

public class HotelReservations {
    private long reservationID;
    private LocalDate checkInDate;
    private LocalDate checkOutDate;
    private int reservationRoom;

    public HotelReservations (long reservationID, LocalDate checkInDate, LocalDate checkOutDate, int reservationRoom) {
        this.reservationID = reservationID;
        this.checkInDate = checkInDate;
        this.checkOutDate = checkOutDate;
        this.reservationRoom = reservationRoom;
    }
    
    public long getReservationID () {
        return reservationID;
    }
    public LocalDate getCheckInDate() {
        return checkInDate;
    }
    public LocalDate getCheckOutDate() {
        return checkOutDate;
    }
    public int getReservationRoom () {
        return reservationRoom;
    }
}
