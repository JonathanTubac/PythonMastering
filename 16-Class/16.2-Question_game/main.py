import data as d
import question as q
import random as rd

#global variables
game = True
current_question = 0
q_number = 1
score = 0
set_questions = True
#Function to choose a random question from the data
def choose_random_question(questions):
    random_index = rd.randint(0, len(questions) - 1)
    random_question = questions[random_index]
    #this avoids to choose the same question each time we use this function
    questions.pop(random_index)
    return random_question


#Initialize objects
questions_game = []

print("Welcome to Questionary!")
while set_questions:
    number_of_questions = int(input("How many questions do you want for the game? (max. 20): "))
    if number_of_questions > 20:
        print("You can't exceed 20!")
        continue
    elif number_of_questions < 1:
        print("you can't enter 0 or negative")
        continue
    else:
        set_questions = False
        
        
for i in range(1, number_of_questions + 1):
    random_question = choose_random_question(d.questions)
    question = q.Question(random_question["text"], random_question["answer"])
    questions_game.append(question)

while game:
    
    if current_question == len(questions_game):
        print("You finished the game!")
        print(f"Your final score {score}/{len(questions_game)}")
        game = False
        continue
    else:
        pass
    
    print(f"-----------Question {q_number}----------")
    print(questions_game[current_question].text)
    user_ans = input("True or False? ").capitalize()
    is_correct = questions_game[current_question].isCorrectAnswer(user_ans)
    
    if is_correct:
        print("Correct!")
        score += 1
    else:
        print("Wrong!")
        pass
    
    current_question += 1
    q_number += 1
    
    input("Press enter to continue.")
    