import java.util.*;

public class Taxi {
    int id;
    static int taxino = 0;
    boolean isBooked;
    char currentspot;
    int freetime;
    int totalEarnings;
    ArrayList<String> trips;

    public Taxi() {
        taxino += 1;
        this.id = taxino;
        this.isBooked = false;
        this.currentspot = 'A';
        this.freetime = 6;
        this.totalEarnings = 0;
        this.trips = new ArrayList<String>();
    }

    public void printTaxiDetails() {
        // print total earningand taxi details like current location and free time
        System.out.println("Taxi - " + this.id + " Total Earnings - " + this.totalEarnings + " Current spot - "
                + this.currentspot + " Free Time - " + this.freetime);
    }

}