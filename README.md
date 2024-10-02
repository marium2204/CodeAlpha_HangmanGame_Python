# CodeAlpha_HangmanGame_Python
Welcome to the Hangman Game, a fun and engaging word-guessing challenge! This game has been designed by Marium Haris and assigned by CodeAlpha, aiming to test your vocabulary and deduction skills.<br>
This program utilizes the Natural Language Toolkit (nltk) to select words from a predefined list of lowercase English words.<br><br>

KEY FEATURES:<br>
Word Selection: The game randomly selects a word with 3 to 6 lowercase letters from the nltk words corpus.<br>
Guessing Mechanism: Players have a total of 5 chances to guess letters in the word.<br>
Scoring System: Each correct guess earns the player 10 points, while each incorrect guess deducts 10 points from their score.<br>
Hints: Players can request hints, with a maximum of 2 hints available, which reveal one of the unguessed letters in the word.<br>
User Input Validation: The game ensures that the input is a single lowercase letter and prevents duplicate guesses.<br><br>

GAME:<br>
Players are introduced to the rules and objectives of the game at the start.<br>
The game loop allows players to guess letters, receive feedback on their guesses, and see their current score and remaining chances.<br>
The game concludes when the player either successfully guesses the word or exhausts their chances.<br><br>

USAGE: <br>
To run the Hangman Game, you'll need Python installed on your computer along with the nltk library.<br>
Install the required library: pip install nltk <br>
Download the NLTK words corpus (if not already installed): <br>
import nltk <br>
nltk.download('words') <br><br>

If you would like to contribute to this project, please feel free to fork the repository and submit a pull request. Suggestions for improvements and additional features are always welcome!
