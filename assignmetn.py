# Student Number: 2425477
# Student Name: Muhammad Usama Riaz
# Module: COM4402

# 1. Initialisation
# We use Python Lists to store the data
questions = [
    "What is the capital of France?",
    "What is 5 + 5?",
    "Which language is used for web style?"
]

options = [
    "A) London, B) Paris, C) Berlin",
    "A) 10, B) 15, C) 20",
    "A) Python, B) HTML, C) CSS"
]

correct_answers = ["B", "A", "C"]

score = 0

# 2. Iteration (The Loop)
# Loop through the questions using range and len
for index in range(len(questions)):

    # 3. Presentation
    print("----------------------------")
    print("Question " + str(index + 1) + ":")
    print(questions[index])
    print(options[index])

    # 4. Input
    # We use .upper() so it accepts 'b' or 'B'
    user_answer = input("Enter your answer (A, B, or C): ").upper()

    # 5. Validation and Scoring
    if user_answer == correct_answers[index]:
        print("Correct!")
        score = score + 1
    else:
        print("Incorrect.")

# 6. Termination
print("----------------------------")
print("Quiz Finished!")
print("Final Score: " + str(score) + " out of " + str(len(questions)))