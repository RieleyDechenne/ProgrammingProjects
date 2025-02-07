import java.util.Scanner;

public class BankProgram {

    static Scanner scanner = new Scanner(System.in);
    
    public static void main(String[] args) {
        //Basic Java Calculator

        // Declare Variables
        double balance = 0;
        boolean isRunning = true;
        int choice;

        // Display Menu
        while (isRunning) { 
            System.out.println("***************");
            System.out.println("BANKING PROGRAM");
            System.out.println("***************");
            System.out.println("1. Show Balance");
            System.out.println("2. Deposit");
            System.out.println("3. Withdraw");
            System.out.println("4. Exit");
            System.out.println("***************");

        // Get and Process user Input
            System.out.print("Enter your choice (1-4): ");
            choice = scanner.nextInt();

            switch (choice) {
                case 1 -> showBalance(balance);
                case 2 -> balance += deposit();
                case 3 -> balance -= withdraw(balance);
                case 4 -> isRunning = false;
                default -> System.out.println("INVALID CHOICE");
            }
        }    

        // Exit message
        System.out.println("***************");
        System.out.println("Thank you, have a wonderful day!");
        System.out.println("***************");

        scanner.close();
    }
        // showBalance()
    static void showBalance(double balance){
        System.out.println("***************");
        System.out.printf("$%.2f\n", balance);
    }
        // deposit()
    static double deposit(){

        double amount;

        System.out.print("Enter the amount you want to deposit: ");
        amount = scanner.nextDouble();

        if (amount < 0) {
            System.out.println("Amount cannot be negative!");
            return 0;
        }
        else{
            return amount;
        }
    }
        // withdraw()
    static double withdraw(double balance){
        double amount;

        System.out.print("Enter amount to be withdrawn: ");
        amount = scanner.nextDouble();

        if (amount > balance) {
            System.out.println("Insufficient Funds!");
            return 0;
        }
        else if (amount < 0) {
            System.out.println("Amount cannot be negative");
            return 0;
        }
        else{
            return amount;
        }
    }
}