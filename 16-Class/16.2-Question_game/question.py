class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer
        
    def isCorrectAnswer(self, user_ans):
        if user_ans == self.answer:
            return True
        else:
            return False