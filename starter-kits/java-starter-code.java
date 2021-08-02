// Happy Birthday MLH //

//Starter Codes for Java Language//

//Hello World//

public class Main
{
	public static void main(String[] args) {
		System.out.println("Hello World");
	}
}


// Sum of Two Numbers //

public class AddTwoNumbers // create class
{ 

   public static void main(String[] args)  //create main method
   {
        
      int num1 = 5, num2 = 15, sum; // declare and initialize variables
      sum = num1 + num2; //store sum of two variables to sum variable

      System.out.println("Sum of these numbers: "+sum); //print sum of two variables
   }
}


// Check if number is even or odd //

import java.io.*; // import java.io.*; for use of BufferedReader

class even
{
  public static void main(String args[]) throws Exception //throws Exception because BufferedReader create an exception
  {
    int num;
	
	BufferedReader br=new BufferedReader(new InputStreamReader(System.in)); //this is used to enter value from user
	
    System.out.println("Enter an Integer number:");
	num=Integer.parseInt(br.readLine());//br.readLine stored only string values so convert it to integer by using Integer.parseInt
	
    /* If number is divisible by 2 then it's an even number
     * else odd number*/
    if ( num % 2 == 0 )
        System.out.println("Entered number is even");
     else
        System.out.println("Entered number is odd");
  }
}


// Find Fibonacci Number//

import java.util.Scanner;

class Process {
    void process() {
        Scanner in = new Scanner(System.in);
        int n;
        double num;
        System.out.println("Find n Fibonachi number");
        System.out.print("Enter n: ");
        n = in.nextInt();
        if(n > 50)
            n = 50;

        System.out.println(fibb(n));
        in.close();
    }
    private long fibb(int n){
        long f0 = 0, f1 = 1;
        if(n == 0)
            return f0;
        if(n == 1)
            return f1;

        for (int i = 2; i < n; i++) {
            long t = f0;
            f0 = f1;
            f1 += t;
        }
        return  f1;
    }
}


// Check if Happy Number or not//

import java.util.ArrayList;
import java.util.Scanner;

class Process {
    private Scanner in = new Scanner(System.in);
    private int n;

    void process() {
        System.out.println("Happy Numbers");
        System.out.print("Enter n: ");
        n = in.nextInt();
        findEightHappyNumbers(n);
    }
    private void findEightHappyNumbers(int n) {
        int count = 0;
        while(count < 8) {
            if(isHappy(n)) {
                System.out.println(n);
                count++;
            }
            n++;
        }
    }
    private boolean isHappy(int n) {
        ArrayList<Integer> history = new ArrayList<>();
        while(n != 1) {
            history.add(n);
            int sum = 0;
            while (n != 0) {
                sum += Math.pow(n%10, 2);
                n /= 10;
            }
            n = sum;
            if(history.contains(n))
                return false;
        }
        return true;
    }
}


// Tax Calculator//

import java.util.Scanner;

public class Tax {
        Scanner in = new Scanner(System.in);
        double cost, tax;
        System.out.println("Tax Calculator");
        System.out.print("Enter the cost: ");
        cost = in.nextDouble();
        System.out.print("Enter country tax: ");
        tax = in.nextDouble();
        System.out.println("Total cost is " + (cost + cost*tax/100));
    }
}


// Find Pi Number//

import java.math.BigDecimal;
import java.math.RoundingMode;
import java.util.Scanner;

class Pi {
	public static void main( String[] args ) {
		Scanner in = new Scanner(System.in);
		BigDecimal bd1, bd2;
		int n;
		double num;
		System.out.println("Find n Pi number");
		System.out.print("Enter n: ");
		n = in.nextInt();
		if(n > 50)
			n = 50;
		num = (16*Math.atan(1./5) - 4*Math.atan(1./239));
		bd1 = new BigDecimal(num);
		bd2 = bd1.setScale(n, RoundingMode.FLOOR);
		System.out.println(bd2);
		in.close();
	}
}




// Hope this Java Source File helped you in getting the key concepts of basic Java programming//
