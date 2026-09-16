
# ----------------- # -- 🎯 Hangman Game -- # ----------------- #

import os
import random
import time


# Clear the console screen
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


# ------------------- # -- Main Func. -- # -------------------- #

divider = " # " + "-" * 30 + " # "

replaying = True

# Hangman drawing for each number of lost lives
HANGMAN_PICS = [
    """
       -----
       |   |
           |
           |
           |
    --------
    """,
    """
       -----
       |   |
       O   |
           |
           |
    --------
    """,
    """
       -----
       |   |
       O   |
       |   |
           |
    --------
    """,
    """
       -----
       |   |
       O   |
       |\\  |
           |
    --------
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
           |
    --------
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
        \\  |
    --------
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
      / \\  |
    --------
    """
]


# Words and their hints
# Use this single word to test the game:
# words = {
#     "developer": "A person who builds software and writes computer code."
# }

words = {
    "python": "A popular programming language named after a giant snake.",
    "developer": "A person who builds software and writes computer code.",
    "pyramids": "Ancient massive triangular stone structures, famous in Egypt.",
    "keyboard": "An input hardware device with keys used for typing.",
    "ocean": "A vast body of salt water that covers most of the Earth."
}

last_game_word = ""


# ----------------- # -- Main Game Loop -- # ----------------- #

while replaying:

    lives = 6
    playing = True

    # Choose a random word and its hint
    chosen_word, hint = random.choice(list(words.items()))

    # Avoid using the same word twice in a row
    if chosen_word == last_game_word:
        continue

    # Hide all letters at the start
    hidden_word = ["_"] * len(chosen_word)

    # Reveal one random letter as a starting hint
    random_index = random.randrange(len(chosen_word))
    start_char = chosen_word[random_index]

    # Reveal all occurrences of the starting letter
    for index, char in enumerate(chosen_word):
        if char == start_char:
            hidden_word[index] = char

    last_game_word = chosen_word


    # ----------------- # -- Current Round -- # ----------------- #

    while playing:

        dash_word = " ".join(hidden_word)

        # Continue while there are hidden letters and remaining lives
        if "_" in hidden_word and lives > 0:
            
            print(divider)
            print("🎯 Welcome to Hangman Game! 🎯")

            print(divider)
            print(HANGMAN_PICS[6 - lives])
            print(divider)

            print(f'💡 Hint: "{hint}" | ❤️ Lives left: [{lives}]')

            print(divider)

            # Get one letter from the player
            the_letter = input(f"-> Guess a letter: {dash_word} : ").lower().strip()

            print(divider)

            # Make sure the input is a single letter
            if len(the_letter) != 1 or not the_letter.isalpha():
                print("⚠️ Please enter a single letter (a-z).")
                time.sleep(2.2)
                clear_screen()
                continue

            # Check if the letter exists in the word
            if the_letter in chosen_word:

                # Prevent guessing an already revealed letter
                if the_letter in hidden_word:
                    print("⚠️ This letter has already been entered.")
                    time.sleep(2.4)
                    clear_screen()
                    continue

                chars = []

                # Reveal all occurrences of the guessed letter
                for index, letter in enumerate(chosen_word):
                    if the_letter == letter:
                        chars.append(index + 1)
                        hidden_word[index] = letter

                # Show where the letter was found
                if len(chars) > 1:
                    print(f'✅ Great answer! The letter "{the_letter}" '
                          f'is found {len(chars)} times.')
                    print(f'📍 Found in positions: '
                          f'[{" - ".join(map(str, chars))}]')

                else:
                    print("✅ Correct Answer!")
                    print(f'📍 Letter [{the_letter}] is found '
                          f'in position: {chars[0]}')

                time.sleep(2)
                

            else:
                # Wrong guesses reduce one life
                print("❌ Wrong letter, try again!")
                lives -= 1
                print(f"❤️‍🩹 Lives - 1\n💝 Lives left: [{lives}]")


            time.sleep(3)
            clear_screen()


        # ----------------- # -- Round Finished -- # ----------------- #

        else:

            print(divider)

            if lives == 0:
                print(f"💀 Game Over! You lost all your lives [{lives}].")
                print(f"🔍 The word was: [{chosen_word.capitalize()}]")

            else:
                print(f"🎉 The Word: {dash_word} "
                      f"=> {chosen_word.capitalize()}")
                print("🏆 You found it! Well Done!")

            print(divider)
            time.sleep(3.7)

            # Ask if the player wants another round
            play_again = input("-> ▶️ Play again? (y or n): ").lower().strip()

            # Keep asking until the input is valid
            while play_again not in ("y", "n"):
                print("⚠️ Invalid input. Please choose (y or n).")
                print(divider)
                time.sleep(2)

                play_again = input("-> ▶️ Play again? (y or n): ").lower().strip()

            if play_again == "y":
                playing = False
                clear_screen()

            else:
                replaying = False
                playing = False


print("🎮 Game Over! Thanks for playing 👋")

# ---------------------------------------------------------- #