import random
import nltk
from nltk.corpus import words

WordList=words.words()

filtered_words=[]
for word in WordList:
    if len(word) <= 6 and len(word)>=3 and word.islower():
        filtered_words.append(word)
word = random.choice(filtered_words)

The_word = ['_'] * len(word)

chances = 5 
wrong_letters = []
right_letters = []  
score=50
hint_count=2

print("                          Welcome to the Hangman Game!")
print("                             Task by Marium Haris")
print("                             Assigned by CodeAlpha")
print("\nRead the following rules:")
print("-> You have 5 chances to guess the right word")
print("-> If you guess a letter correctly, it will be filled in the word.")
print("-> If you guess a letter incorrectly, it will be added to the wrong letters list. The list will be shown to you.")
print("-> For each correct guess 10 points will be added to your score.")
print("-> For each wrong guess 10 points will be deducted from your score.")
print("-> Only 2 letter hints will be provided.")

for i in range(1,20):
    if chances <= 0:
        break
    print("\n"+ "guess "+ str(i) +": ")
    print("The word is: "+ ' '.join(The_word))
    print("Current Score: ", score)
    print("Chances left: ",chances)
    print("Hints left: ",hint_count)
    guess=input("Guess a letter or type 'hint' for a letter hint: ")

    if guess=="hint":
        if hint_count>0:
            hint_count-=1
            Unguessed_letter=[letter for letter in set(word) if letter not in right_letters and letter not in wrong_letters]
            if Unguessed_letter:
                hint_letter=random.choice(Unguessed_letter)
                print("Hint: One of the letters in the word is ",hint_letter)
            continue
        else:
            print("You have used all your hints. Guess a letter now.")
            continue

    if len(guess) != 1 or not guess.isalpha() or not guess.islower():
        print("Invalid input. Please enter a single, lowercase letter.")
        continue

    if guess in right_letters or guess in wrong_letters:
        print("You already guessed that letter. Try a different letter!")
        continue
    
    if guess in word:
        right_letters.append(guess)
        score+=10

        for i in range(len(word)):
            if word[i] == guess:
                The_word[i] = guess
                
        if "_" not in The_word:
            print("\nCongratulations! You've guessed the word. The word is:", word)
            print("Your final score is: ", score)
            break
    else:
        chances -= 1
        print(guess+" is not the letter of the word.")
        wrong_letters.append(guess)
        print("Wrong guesses you've already made: "+' '.join(wrong_letters))
        score-=10

if chances == 0:
    print("\nNo chances left! The word was:", word)
    print("Your final score is: ", score)
