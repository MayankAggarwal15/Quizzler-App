import requests , html

class QuestionBank():

    def __init__(self):

        self.count = 0
        self.response = requests.get("https://opentdb.com/api.php?amount=10&type=boolean")
        self.response.raise_for_status()

        self.quiz_data = self.response.json()
        self.question_data = self.quiz_data["results"]

    def question(self):
        self.count += 1
        
        quiz_ques = html.unescape(f"Q{self.count}. {self.question_data[self.count-1]['question']} (True ✔ / False ✖)")
        return quiz_ques

    def answer(self):
        correct_answer = self.question_data[self.count-1]["correct_answer"]
        return correct_answer