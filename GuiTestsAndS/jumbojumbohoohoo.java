//This is me first file de JAVA

import java.io.*;

class DemoPrint{
    public static <str> void main (String[] args)
    {
        System.out.println("Hello World");
        //str c;
        int a = System.in.println("Input first number");
        int b = System.in.println("Input second number");
        //c = System.in.println("Input opperation to be performed");
        if (a == b ){
            System.out.println("Both numbers are equal");
        }
        else{
        int b1 = b;
        if (a > b1 ){
            System.out.println("First number is greater");
        }
        else{
            System.out.println("Second number is greater");
        }
    }
    }
}