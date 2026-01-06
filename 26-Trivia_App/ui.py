from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class QuizInterface:
    
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title = "Quizz"
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        
        self.score_label = Label(text="Score: ", bg=THEME_COLOR, fg="white", font=("Arial", 14, "bold"))
        self.score_label.grid(column=1, row=0)
        
        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
    
        self.question_text = self.canvas.create_text(150, 125, width=300, text="Questions goes here", fill=THEME_COLOR, font=("Arial", 20, "italic"))
        
        true_image = PhotoImage(file="./26-Trivia_App/images/true.png")    
        self.true_btn = Button(image=true_image, command=self.true_presed)
        self.true_btn.grid(column=0, row=2)
        
        false_image = PhotoImage(file="./26-Trivia_App/images/false.png")
        self.false_btn = Button(image=false_image, command=self.false_pressed)
        self.false_btn.grid(column=1, row=2)
        
        self.get_question_text()
        self.window.mainloop()
    
    def get_question_text(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            question = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=question)
        else:
            self.canvas.itemconfig(self.question_text, text=f"You completed the quiz, Score: {self.quiz.score}/{len(self.quiz.question_list)}")
            self.true_btn.config(state="disabled")
            self.false_btn.config(state="disabled")

    
    def true_presed(self):
        is_right = self.quiz.check_answer("True")
        self.show_answer_to_user(is_right)
        
    def false_pressed(self):
        is_false = self.quiz.check_answer("False")
        self.show_answer_to_user(is_false)
    
    def show_answer_to_user(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_question_text)