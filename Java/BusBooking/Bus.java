package BusBooking;

import java.util.*;

public class Bus {
    static int id=0;
    int busId=0;
    int capacity=50;
    ArrayList<String> passengerNames;

    public Bus(){
        id=id+1;
        busId=id;
        passengerNames = new ArrayList<String>();
    }
}
