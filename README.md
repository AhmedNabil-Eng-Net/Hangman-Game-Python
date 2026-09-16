# 🎯 Hangman Game

A simple command-line Hangman game built with Python.

## ✨ Features

* 🎲 Randomly select a word from a predefined list
* 💡 Display a hint for each word
* ❤️ Start each round with 6 lives
* 🔤 Guess one letter at a time
* 🔁 Handle repeated and invalid guesses
* 📍 Show the positions of repeated letters
* 🎨 Display a Hangman drawing based on remaining lives
* 🔄 Play multiple rounds

## 🛠️ Technologies

* Python
* `random` module
* `time` module
* `os` module
* Lists
* Dictionaries
* Loops
* Conditional Statements
* String Methods
* `enumerate()`
* `map()`
* Input Validation

## 🚀 How to Run

Make sure Python is installed on your computer.

Run the game with:

```bash
main.py
```

## 🎮 How to Play

1. The game randomly selects a word and displays a hint.
2. One random letter is revealed at the beginning.
3. Guess one letter at a time.
4. A wrong guess costs one life.
5. The game ends when you:

   * Reveal all letters and win 🏆
   * Lose all 6 lives 💀
6. After each round, you can choose whether to play again.

### Example

```text
💡 Hint: "A popular programming language named after a giant snake."
❤️ Lives left: [6]

-> Guess a letter: _ y _ h _ n : p

✅ Correct Answer!
📍 Letter [p] is found in position: 1
```

## ➕ Adding More Words

You can easily add more words and hints to the `words` dictionary:

```python
words = {
    "python": "A popular programming language named after a giant snake.",
    "developer": "A person who builds software and writes computer code.",
    "keyboard": "An input hardware device with keys used for typing."
}
```

## 📚 What I Practiced

This project helped me practice:

* Working with lists and dictionaries
* Random selection with `random.choice()` and `random.randrange()`
* Using `enumerate()` to track positions
* Converting values with `map()`
* Using `.join()`, `.lower()`, `.strip()`, and `.isalpha()`
* Nested `while` loops
* Input validation
* Managing game state with variables
* Basic console UI and animations

## 👨‍💻 Author

  **Ahmed Nabil**
