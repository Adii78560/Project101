import java.util.Scanner;

class VirtualPet {
    private String name;
    private int hunger;
    private int mood;

    public VirtualPet(String name) {
        this.name = name;
        this.hunger = 50;
        this.mood = 50;
    }

    public void feed() {
        hunger -= 20;
        mood += 10;
        if (hunger < 0) hunger = 0;
        if (mood > 100) mood = 100;
    }

    public void play() {
        hunger += 10;
        mood += 30;
        if (hunger > 100) hunger = 100;
        if (mood > 100) mood = 100;
    }

    public void status() {
        System.out.println("Pet Name: " + name);
        System.out.println("Hunger Level: " + hunger);
        System.out.println("Mood Level: " + mood);
    }
}

public class VirtualPetSimulator {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Welcome to Virtual Pet Simulator!");
        System.out.print("Enter your pet's name: ");
        String petName = scanner.nextLine();

        VirtualPet pet = new VirtualPet(petName);

        while (true) {
            System.out.println("\nWhat do you want to do?");
            System.out.println("1. Feed " + petName);
            System.out.println("2. Play with " + petName);
            System.out.println("3. Check " + petName + "'s status");
            System.out.println("4. Exit");

            int choice = scanner.nextInt();
            scanner.nextLine(); // Consume the newline character after reading the integer input.

            switch (choice) {
                case 1:
                    pet.feed();
                    break;
                case 2:
                    pet.play();
                    break;
                case 3:
                    pet.status();
                    break;
                case 4:
                    System.out.println("Thanks for playing! Goodbye!");
                    scanner.close();
                    System.exit(0);
                default:
                    System.out.println("Invalid choice! Please try again.");
            }
        }
    }
}
