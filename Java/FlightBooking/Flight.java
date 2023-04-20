package FlightBooking;

import java.util.*;

public class Flight {
    static int id = 0;
    int flightId;
    int availableSeats;
    int price;
    ArrayList<String> passengerDetails;

    public Flight() {
        id += 1;
        flightId = id;
        availableSeats = 50;
        price = 5000;
        passengerDetails = new ArrayList<String>();
    }

}
