import java.util.Scanner;

public class mortgage_calculator {
    public static void Main(String[] args) {
        Scanner principal = new Scanner(System.in);
        System.out.print("Principal: ");
        int principalValue = principal.nextInt();
        Scanner annualInterestRate = new Scanner(System.in);
        System.out.print("Annual Interest Rate: ");
        float annualInterestRateValue = annualInterestRate.nextFloat();
        Scanner period = new Scanner(System.in);
        System.out.print("Period (Years): ");
        int periodValue = period.nextInt();

    }
}
