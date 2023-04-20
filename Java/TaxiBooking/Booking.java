import java.util.*;

public class Booking {
    public static void setDetails(Taxi t, boolean booked, char currentSpot, int freeTime, int Earnings,
            String tripDetail) {
        t.isBooked = booked;
        t.currentspot = currentSpot;
        t.freetime = freeTime;
        t.totalEarnings += Earnings;
        t.trips.add(tripDetail);
    }

    public static void booking(ArrayList<Taxi> freetaxis, int pid, char pickupPoint, char destination, int ptime) {
        Taxi minTaxi = null;
        int min = 1000;
        String tripDetail = "";
        for (Taxi t : freetaxis) {
            int s = Math.abs(t.currentspot - pickupPoint) + t.freetime;
            if (s < min) {
                minTaxi = t;
                min = s;
            }
        }
        int distanceBetweenpickUpandDrop = Math.abs((destination - '0') - (pickupPoint - '0')) * 15;
        int earning = (distanceBetweenpickUpandDrop - 5) * 10 + 100;
        int dropTime = ptime + distanceBetweenpickUpandDrop / 15;
        int nextfreeTime = dropTime;
        char nextSpot = destination;
        tripDetail = pid + "               " + pid + "          " + pickupPoint + "      "
                + destination + "       " + ptime + "          " + dropTime + "           " + earning;
        setDetails(minTaxi, true, nextSpot, nextfreeTime, earning, tripDetail);
        System.out.println("Taxi " + minTaxi.id + " booked");
    }

    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        int n = s.nextInt();
        ArrayList<Taxi> taxis = new ArrayList<Taxi>();
        for (int i = 0; i < n; i++) {
            taxis.add(new Taxi());
        }

        while (true) {
            System.out.println("Enter 1 to book or 2 to printDetails or 3 to exit");
            int choice = s.nextInt();
            switch (choice) {
                case 1:
                    System.out.println("Enter PassengerId");
                    int pid = s.nextInt();
                    System.out.println("Enter PickupTime");
                    int ptime = s.nextInt();
                    System.out.println("Enter PickUpPoint");
                    char pickupPoint = s.next().charAt(0);
                    System.out.println("Enter Destination");
                    char destination = s.next().charAt(0);
                    if (pickupPoint < 'A' || destination > 'F' || pickupPoint > 'F' || destination < 'A') {
                        System.out.println("Valid pickup and drop are A, B, C, D, E, F. Exitting");
                        return;
                    }
                    ArrayList<Taxi> freetaxis = new ArrayList<>();
                    for (Taxi t : taxis) {
                        if (t.freetime <= ptime && (t.freetime + Math.abs(t.currentspot - pickupPoint)) <= ptime) {
                            freetaxis.add(t);
                        }

                    }
                    if (freetaxis.size() == 0) {
                        System.out.println("No Taxi can be alloted. Exitting");
                        return;
                    }
                    Collections.sort(freetaxis, (a, b) -> a.totalEarnings - b.totalEarnings);
                    booking(freetaxis, pid, pickupPoint, destination, ptime);
                    break;
                case 2:
                    for (Taxi t : taxis)
                        t.printTaxiDetails();
                    return;
                default:
                    return;
            }

        }
    }
}