# Python Quiz Game

questions = ("How many elements are there in the periodic table: ",
             "Which animal lays the largest eggs: ",
             "Which gas is most abundant in the atmosphere of Earth: ",
             "How many bones are there in human body: ",
             "Which planet in the solar system is the hottest: "
             )

Options = (("A.116 ", "B.111 ", "C.117 ", "D.118 "),
           ("A.Whale ", "B. Crocodile", "C.Ostrich ", "D.Alligator "),
           ("A.Hydrogen ", "B.Oxygen ", "C.Nitrogen ", "D. Carbon Dioxide"),
           ("A.209 ", "B.208 ", "C.106 ", "D.206 "),
           ("A. Mecrury", "B. Venus", "C. Earth", "D. Mars"))

answers = ("D", "C", "C", "D","B")
guesses = []
question_num = 0 
score = 0 

for question in questions:
    print("-----------------------------------------------")
    print(question)
    for option in Options[question_num]:
        print(option)

    guess = input("Enter A,B,C,D: ").upper()
    guesses.append(guess) 
    if guess == answers[question_num]:
        score += 1
        print("Correct")
    else:
        print(f"{answers[question_num]} is the correct answer")

    question_num += 1

print(f"Your final score is {score} out of {len(questions)}")