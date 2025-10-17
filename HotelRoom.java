public class HotelRoom {
    private int roomNumber;
    private String occupant;
    private double pricePerNight;
    private boolean isBooked;

    public HotelRoom (int roomNumber, String occupant, double pricePerNight, boolean isBooked) {
        this.roomNumber = roomNumber;
        this.occupant = occupant;
        this.pricePerNight = pricePerNight;
        this.isBooked = isBooked;
    }
    public int getRoomNumber () {
         return roomNumber;
    }
    public String getOccupantName () {
        return occupant;
    }
    public double getPricePerNight () {
        return pricePerNight;
    }
    public boolean isBooked () {
        return isBooked;
    }
}
