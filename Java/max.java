import java.util.Iterator;
import java.util.*;

public class max {
    public static void main(String[] args){
  String str1="apple";
  String str2="orange";
  String str3="";
  TreeSet<Character> charSet = new TreeSet<Character>();
  for(int i=0; i<str1.length(); i++){
    charSet.add(str1.charAt(i));
  }
  for(int i=0; i<str2.length(); i++){
    charSet.add(str2.charAt(i));
  }
  Iterator i=charSet.descendingIterator();
  while(i.hasNext()) {  
str3+=(i.next());  
}
System.out.println(str3);
}}
