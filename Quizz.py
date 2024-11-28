# ----------------------------------------------------------------

def new_game():
    guesses = []
    correct_guesses = 0
    question_num = 1

    for question, answer in questions.items():
        print('----------------------------------')
        print(question)
        for option in options[question_num]:
            print(option)
        guess = input("Enter (A, B, C, or D): ").upper()
        guesses.append(guess)

        correct_guesses += check_answer(answer, guess)
        question_num += 1

    display_score(correct_guesses, guesses)

# ----------------------------------------------------------------

def check_answer(answer, guess):
    if answer == guess:
        print("Correct!")
        return 1
    else:
        print("Incorrect!")
        return 0

# ----------------------------------------------------------------

def display_score(correct_guesses, guesses):
    print("--------------------------------")
    print("Results")
    print("--------------------------------")

    print("Answers: ", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("Guesses: ", end="")
    for i in guesses:
        print(i, end=" ")
    print()

    score = int((correct_guesses/len(questions)) * 100)
    print("Your score is: " + str(score) + "%")

# ----------------------------------------------------------------

def play_again():
    response = input("Do you want to play again? (yes or no): ").lower()
    return response == "yes"

questions = {
"Who created Python?: " : "A",
"What year was Python created?: " : "B",
"Python is attributed to which comedy group?: " : "C",
"Is the Earth round?: " : "A",
}

options = {
    1: ["A. Guido van Rossum", "B. Elon Musk", "C. Bill Gates", "D. Mark Zuckerberg"],
    2: ["A. 1989", "B. 1991", "C. 2000", "D. 2016"],
    3: ["A. Lonely Island", "B. Smosh", "C. Monty Python", "D. SNL"],
    4: ["A. True", "B. False", "C. Sometimes", "D. What's Earth?"]
}

new_game()

while play_again():
    new_game()

print("Byeeee!")
