public class HotelGuest {
    private String guestName;
    public long reservationID;
    public HotelGuest (String guestName, long reservationid) {
        HotelReservations reservationiD = new HotelReservations();
        this.reservationID = reservationiD.getReservationID();
        this.guestName = guestName;
    }
    
    public String getGuestName () {
        return guestName;
    }
    public long getReservationID () {
        return reservationID;
    }
}
