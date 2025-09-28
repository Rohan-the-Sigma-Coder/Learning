import java.text.NumberFormat;
import java.util.Scanner;

public class mortgage_calculator {
    public static void main(String[] args) {
        final byte MONTHS_IN_YEAR = 12;
        final byte PERCENT = 100;

        Scanner scanner = new Scanner(System.in);
        
        int principal = scanner.nextInt();
        float annualInterest = scanner.nextFloat();
        byte years = scanner.nextByte();

        System.out.println("Principal ($1K = $1M): ");
        while (principal < 1_000 || principal > 1_000_000) {
            System.out.println("Enter a number between 1,000 and 1,000,000.");
            System.out.println("Principal ($1K = $1M): ");
        }
        System.out.print("Annual Interest Rate: ");
        while (annualInterest < 0 || annualInterest > 30) {
            System.out.println("Enter a value greater than 0 and less than or equal to 30.");
            System.out.print("Annual Interest Rate: ");
        }
        float monthlyInterest = annualInterest / PERCENT / MONTHS_IN_YEAR;
            
        System.out.print("Period (Years): ");
        while (years < 0 || years > 30) {
            System.out.println("Enter a value between 1 and 30.");
            System.out.print("Period (Years): ");
        }
            
        int numberOfPayments = years * MONTHS_IN_YEAR;
            
        double mortgage = principal * (monthlyInterest * Math.pow(1 + monthlyInterest, numberOfPayments)) / ((Math.pow(1 + monthlyInterest, numberOfPayments)) - 1);
        System.out.println(NumberFormat.getCurrencyInstance().format(mortgage));

        }
    }

