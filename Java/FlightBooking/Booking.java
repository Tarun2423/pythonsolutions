package FlightBooking;

import java.util.*;

public class Booking {
    public static void bookTicket(Flight currFlight, int pid, int bt) {
        int price = currFlight.price;
        currFlight.availableSeats -= bt;
        System.out.println("Amount to be paid=" + bt * price);
        System.out.println("Booked SuccessFully");
        System.out.println("Price=" + currFlight.price);
        System.out.println("Seats Available=" + currFlight.availableSeats);
        String details = "The Passenger " + pid + " booked " + bt + " tickets and paid " + bt * price;
        currFlight.passengerDetails.add(details);
        currFlight.price += (200 * bt);
        printDetails(currFlight.passengerDetails);
        System.out.println("CuurentTicketPrice=" + currFlight.price);

    }

    public static void printDetails(ArrayList<String> passengerDetails) {
        for (String pd : passengerDetails) {
            System.out.println(pd);
        }
    }

    public static void main(String args[]) {
        ArrayList<Flight> flights = new ArrayList<Flight>();
        for (int i = 1; i < 3; i++) {
            Flight f = new Flight();
            flights.add(f);
        }

        Scanner sc = new Scanner(System.in);
        while (true) {
            System.out.println("Enter '1' - For Booking  , '2' - For Exit");
            int choice = sc.nextInt();
            switch (choice) {
                case 1: {
                    System.out.println("Enter the PassengerId");
                    System.out.println("Enter the Flight Id");
                    int pid = sc.nextInt();
                    int fid = sc.nextInt();
                    if (fid > 2) {
                        System.out.println("Choose a Valid Flight Id to Book");
                    }
                    System.out.println("Enter the number of tickets to be Booked");
                    int bt = sc.nextInt();
                    Flight currflight = null;
                    for (Flight f : flights) {
                        if (f.flightId == fid) {
                            currflight = f;
                            break;
                        }
                    }
                    System.out.println(currflight.flightId);
                    if (bt > currflight.availableSeats) {
                        System.out.println("Tickets not available");
                    } else {
                        bookTicket(currflight, pid, bt);
                    }
                }
            }
        }

    }
}
