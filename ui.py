from tkinter import *
from data import QuestionBank

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self):

        self.quiz = QuestionBank()
        self.ques_count = 0
        self.score = 0
        self.answer = None

        self.window = Tk()
        self.window.title("QUIZZLER APP")
        self.window.config(padx=50, pady=30 , bg=THEME_COLOR)

        self.score_label = Label(text = f"SCORE : {self.score}" , fg="white" , bg=THEME_COLOR , font=("Cambria" , 30 , "bold") )
        self.score_label.grid(row=0 , column=1 , columnspan=2)

        self.canvas = Canvas(width=300 , height=300 , highlightthickness=0 , bg="white")
        self.canvas.grid(row=1 , column=1 , columnspan=2 , pady= 30)
        self.quiz_text = self.canvas.create_text(150 , 150 , text="STATRING QUIZ" , fill="black" , font=("Calibri" , 20 , "bold") , width=280)

        self.true_img = PhotoImage(file="C:/Users/Mayank Aggarwal/Software Development/MAYANK/PYTHON PROGRAMMING/API/QUIZZLER APP/images/true.png")
        self.false_img = PhotoImage(file="C:/Users/Mayank Aggarwal/Software Development/MAYANK/PYTHON PROGRAMMING/API/QUIZZLER APP/images/false.png")

        self.true_button = Button(image= self.true_img , highlightthickness=0 , command= self.true , bd=5)
        self.false_button = Button(image= self.false_img , highlightthickness=0 , command= self.false , bd=5)

        self.true_button.grid(row=2 , column=2)
        self.false_button.grid(row=2 ,column=1)

        self.window.after(1000 , self.next_question)

        self.window.mainloop()


    def true(self):
        self.answer = "True"
        self.feedback()


    def false(self):
        self.answer = "False"
        self.feedback()

    def feedback(self):
        self.true_button.config(state= "disabled")
        self.false_button.config(state= "disabled")
        
        correct_answer = self.quiz.answer()

        if self.answer == correct_answer:
            self.score +=1
            self.canvas.config(bg="green")

        else:
            self.canvas.config(bg="red")
        
        self.window.after(1000 , self.next_question)


    def next_question(self):
        self.true_button.config(state="active")
        self.false_button.config(state="active")

        self.ques_count += 1

        self.canvas.config(bg="white")
        self.score_label.config(text=f"SCORE : {self.score}")

        if self.ques_count <= 10 :
            quiz_ques = self.quiz.question()
            self.canvas.itemconfig(self.quiz_text , text= quiz_ques)
        else:
            self.canvas.itemconfig(self.quiz_text, text="THE END")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    