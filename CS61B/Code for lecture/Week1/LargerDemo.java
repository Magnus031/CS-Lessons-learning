/** Demonstrates creation of a method in Java  */
public class LargerDemo {
    /** Returns the larger of x and y */
    public static int larger(int x,int y){
        if(x>y){
            return x;
        }
        return y;
    }
    public static void main(String[] args){
        System.out.println(larger(-5,10));
    }
}
/*
1.Funcitons must be declared as part of a class in java
  A function that is part of a class is called a "method"
  So in Java,all functions are methods.
2.To define a function in Java,we use "public static".we will 
  see alternate ways of defining functions later.
3.All parameters of a funtion must have a declared type.And the 
  return value of the functions must have a declared type.

*/
