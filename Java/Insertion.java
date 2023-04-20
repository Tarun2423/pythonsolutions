import java.util.*;
class Insertion{
public static void main(String args[]){
    System.out.println("Hello");
    int[] arr=new int[]{5,4,3,2,1};
    System.out.println(Arrays.toString(arr));

    for(int i=1;i<arr.length;i++){
        int curr=arr[i];
        int j=i-1;
        while(j>=0 && arr[j]>curr){
            arr[j+1]=arr[j];
            j--;
        }
        arr[j+1]=curr;
    }
    System.out.println(Arrays.toString(arr));
}
}