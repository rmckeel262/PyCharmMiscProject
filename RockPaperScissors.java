import java.util.Random;
import java.util.Scanner;

public class RockPaperScissors {
    private static final String[] CHOICES = {"rock", "paper", "scissors"};
    private static final Random random = new Random();

    private int playerScore = 0;
    private int computerScore = 0;

    public static void main(String[] args) {
        RockPaperScissors game = new RockPaperScissors();
        game.play();
    }

    public void play() {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Welcome to Rock, Paper, Scissors!");
        System.out.println("----------------------------------------");

        while (true) {
            System.out.printf("%nScore - You: %d | Computer: %d%n", playerScore, computerScore);
            System.out.println("----------------------------------------");
            System.out.print("\nEnter your choice (rock/paper/scissors) or 'quit' to exit: ");

            String playerChoice = scanner.nextLine().toLowerCase().trim();

            if (playerChoice.equals("quit")) {
                System.out.printf("%nFinal Score - You: %d | Computer: %d%n", playerScore, computerScore);
                System.out.println("Thanks for playing!");
                break;
            }

            if (!isValidChoice(playerChoice)) {
                System.out.println("Invalid choice! Please choose rock, paper, or scissors.");
                continue;
            }

            String computerChoice = CHOICES[random.nextInt(CHOICES.length)];

            System.out.println("\nYou chose: " + playerChoice);
            System.out.println("Computer chose: " + computerChoice);

            int result = determineWinner(playerChoice, computerChoice);

            if (result == 0) {
                System.out.println("It's a tie!");
            } else if (result == 1) {
                System.out.println("You win this round!");
                playerScore++;
            } else {
                System.out.println("Computer wins this round!");
                computerScore++;
            }
        }

        scanner.close();
    }

    private boolean isValidChoice(String choice) {
        for (String valid : CHOICES) {
            if (valid.equals(choice)) {
                return true;
            }
        }
        return false;
    }

    private int determineWinner(String player, String computer) {
        if (player.equals(computer)) {
            return 0; // Tie
        }

        if ((player.equals("rock") && computer.equals("scissors")) ||
            (player.equals("scissors") && computer.equals("paper")) ||
            (player.equals("paper") && computer.equals("rock"))) {
            return 1; // Player wins
        }

        return -1; // Computer wins
    }
}
