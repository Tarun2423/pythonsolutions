package BusBooking;

import java.util.*;

public class Booking {
    
public static void printDetails(ArrayList<Bus> buses){
    for(Bus b: buses){
        System.out.println(b.busId + " " + " " + b.capacity);

    }

}
    
public static void printPassengerDetails(ArrayList<Bus> buses,int busno){
    Bus CurrentBus = null;
    for(Bus b: buses){
        if(b.busId==busno){
            CurrentBus = b;
            break;
        }
    }
        for(String c: CurrentBus.passengerNames){
        System.out.println(c);
        }
    
}


public static void bookTicket(int busNo, String Name, ArrayList<Bus> buses){
    Bus CurrentBus =null;
    for(Bus b: buses){
        if(b.busId == busNo){
            CurrentBus = b;
            break;
        }
    }
    if (CurrentBus.capacity>0){
    CurrentBus.passengerNames.add(Name);
    CurrentBus.capacity -= 1;
    System.out.println("Tickets Booked Successfully");
    }
    else{
        System.out.println("Sorry no seats available");
    }
}





    public static void main(String[] args) {
        ArrayList<Bus> buses = new ArrayList<>();
            for(int i = 0; i < 2; i++) {
                buses.add(new Bus());
            }



            while(true){
                System.out.println("Enter your choice...");
                System.out.println("1: Booking, 2: Show Bus Details, 3: Show Passenger Details , 4: Exit");
                Scanner sc=new Scanner(System.in);
                int choice=sc.nextInt();
                switch(choice){
                    case 1:
                    System.out.println("Enter the Bus Number");
                    int busNo=sc.nextInt();
                    if(busNo>2){
                        System.out.println("Please Enter Valid Bus Number");
                    }
                    System.out.println("Enter your Name");
                    String passengerName = sc.next();
                    bookTicket(busNo,passengerName, buses);
                    break;
                    case 2:
                    printDetails(buses);
                    break;
                    case 3:
                    System.out.println("Enter the BusNo...");
                    int busno=sc.nextInt();
                    printPassengerDetails(buses,busno);
                    break;
                    case 4:
                    break;
                }
            }
    }

}
