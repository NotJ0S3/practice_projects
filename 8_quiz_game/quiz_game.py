# 🐍 PYTHON QUIZ GAME

# First let's to declare our variables

# The questions, the options to answer, the correct answer, the score,
# the guesses and the question number

questions = ("1. What is the capital of France?",
            "2. Who wrote the play Romeo and Juliet?",
            "3. What is the largest planet in our solar system?",
            "4. Which element has the chemical symbol 'O'?",
            "5. What is the smallest continent by land are?")

options = ( ("A) Madrid", "B) Rome", "C) Paris", "D) Berlin"),
            ("A) Charles Dickens", "B) William Shakespeare", "C) Mark Twain", "D) Jane Austen"),
            ("A) Earth", "B) Mars", "C) Jupiter", "D) Saturn"), 
            ("A) Oxygen", "B) Gold", "C) Osmium", "D) Helium"), 
            ("A) Europe", "B) Antarctica", "C) Australia", "D) South America"))

answers = ("C", "B", "C", "A", "C")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("----------------------------")
    print(question)
    for option in options[question_num]:
        print(option)
    
    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT! 💚")
    else:
        print("INCORRECT! 💔")
        print(f"{answers[question_num]} is the correct answer")
    question_num += 1
    
print("----------------------------")
print("           RESULTS          ")
print("----------------------------")

print("Answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("Guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score / len/questions * 100)
print(f"Your score is: {score}%")