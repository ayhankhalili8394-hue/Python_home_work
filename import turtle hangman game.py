import turtle
import random

# start

words = [
    "apple",
    "computer",
    "python",
    "piano",
    "guitar",
    "school",
    "planet",
    "rocket",
    "dragon",
    "castle",
    "window",
    "keyboard",
    "elephant",
    "chocolate",
    "adventure"
]

word = random.choice(words)

screen = turtle.Screen()
screen.title("Turtle Hangman")
screen.setup(width=800, height=600)

pen = turtle.Turtle()
pen.speed(0)
pen.pensize(4)
pen.hideturtle()

# Chances display

chances_left = 6

chances_text = turtle.Turtle()
chances_text.hideturtle()
chances_text.penup()
chances_text.goto(0, 250)


def update_chances():
    chances_text.clear()
    chances_text.write(
        "Chances: " + str(chances_left) + "/6",
        align="center",
        font=("Arial", 24, "bold")
    )


# Hangman drawing

def draw_base():
    pen.penup()
    pen.goto(-250, -200)
    pen.pendown()
    pen.goto(0, -200)

    pen.penup()
    pen.goto(-125, -200)
    pen.pendown()
    pen.goto(-125, 200)

    pen.goto(100, 200)
    pen.goto(100, 150)


def draw_head():
    pen.penup()
    pen.goto(100, 100)
    pen.pendown()
    pen.circle(50)


def draw_body():
    pen.penup()
    pen.goto(100, 100)
    pen.pendown()
    pen.goto(100, -50)


def draw_left_arm():
    pen.penup()
    pen.goto(100, 50)
    pen.pendown()
    pen.goto(40, 0)


def draw_right_arm():
    pen.penup()
    pen.goto(100, 50)
    pen.pendown()
    pen.goto(160, 0)


def draw_left_leg():
    pen.penup()
    pen.goto(100, -50)
    pen.pendown()
    pen.goto(40, -120)


def draw_right_leg():
    pen.penup()
    pen.goto(100, -50)
    pen.pendown()
    pen.goto(160, -120)


def draw_hangman(number):
    if number == 1:
        draw_head()
    elif number == 2:
        draw_body()
    elif number == 3:
        draw_left_arm()
    elif number == 4:
        draw_right_arm()
    elif number == 5:
        draw_left_leg()
    elif number == 6:
        draw_right_leg()


# Word display

def show_word(letters):
    word_text.clear()

    word_text.goto(0, -270)

    display = " ".join(letters)

    word_text.write(
        display,
        align="center",
        font=("Arial", 28, "normal")
    )


word_text = turtle.Turtle()
word_text.hideturtle()
word_text.penup()


def win_message():
    message = turtle.Turtle()
    message.hideturtle()
    message.penup()
    message.goto(0, 210)
    message.write(
        "YOU WIN!",
        align="center",
        font=("Arial", 30, "bold")
    )


def lose_message():
    message = turtle.Turtle()
    message.hideturtle()
    message.penup()
    message.goto(0, 210)
    message.write(
        "YOU LOSE! Word: " + word,
        align="center",
        font=("Arial", 24, "bold")
    )


# Start the game

draw_base()

mode = screen.textinput(
    "Hangman",
    "Choose your mode:\n\n"
    "1 = Guess the whole word\n"
    "2 = Guess letter by letter"
)


# Whole-word mode

if mode == "1":

    chances = screen.numinput(
        "Chances",
        "How many chances?\nEnter 1 or 2:",
        minval=1,
        maxval=2
    )

    if chances is not None:
        chances = int(chances)

        for attempt in range(chances):

            guess = screen.textinput(
                "Guess the word",
                "Guess the whole word:"
            )

            if guess is None:
                break

            guess = guess.lower()

            if guess == word:
                show_word(word)
                win_message()
                break

            remaining = chances - attempt - 1

            if remaining > 0:
                screen.textinput(
                    "Wrong!",
                    "Wrong guess!\n"
                    + str(remaining)
                    + " chance(s) remaining."
                )

        else:
            lose_message()


# Letter-by-letter mode

elif mode == "2":

    guessed_letters = []
    revealed = ["_"] * len(word)

    update_chances()
    show_word(revealed)

    while chances_left > 0:

        guess = screen.textinput(
            "Guess a letter",
            "Guess ONE letter:\n\n"
            + " ".join(revealed)
        )

        if guess is None:
            break

        guess = guess.lower()

        if len(guess) != 1 or not guess.isalpha():
            screen.textinput(
                "Invalid",
                "Please enter exactly ONE letter."
            )
            continue

        if guess in guessed_letters:
            screen.textinput(
                "Already guessed",
                "You already guessed that letter!"
            )
            continue

        guessed_letters.append(guess)

        if guess in word:

            for i in range(len(word)):
                if word[i] == guess:
                    revealed[i] = guess

            show_word(revealed)

            if "_" not in revealed:
                win_message()
                break

        else:

            chances_left -= 1

            update_chances()
            draw_hangman(6 - chances_left)

            if chances_left > 0:
                screen.textinput(
                    "Wrong!",
                    "That letter is not in the word."
                )

    else:
        lose_message()


else:
    screen.textinput(
        "Invalid choice",
        "Please restart the game and choose 1 or 2."
    )


screen.mainloop()