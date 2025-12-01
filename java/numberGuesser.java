import java.util.Scanner;

public class NumberGuesser {
    public static void sleep() {
        try {
                Thread.sleep(1500);
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt(); 
                System.out.println("Thread was interrupted during sleep.");
            }
    }
    public static void main(String[] args) {
        int guess = 0;
        int numberOfTriesDone = 0;
        Scanner scanner = new Scanner(System.in);
        System.out.print("How many tries do you want: ");
        int totalNumberOfTries = scanner.nextInt();
        System.out.println("Generating a random number between 1 and 100...");
        sleep();
        int targetNumber = (int)(Math.random() * 100) + 1;
        while (true) {
            numberOfTriesDone += 1;
            if (numberOfTriesDone == totalNumberOfTries) {
                System.out.println("You lose, the number was: " + targetNumber);
                System.exit(1);
            }
            for (int i = 1; i < totalNumberOfTries; i++) {
                System.out.print("Tries left: " + (totalNumberOfTries - numberOfTriesDone) + "Guess: ");
                guess = scanner.nextInt();
                if (guess == targetNumber) {
                    System.out.println("You win!");
                    System.exit(0);   
                }
                else if (guess > targetNumber) {
                    System.out.println("Too high.");
                }
                else {
                    System.out.println("Too low.");
                }
            }
        }
    }
}