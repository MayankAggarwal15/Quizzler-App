# PROJECT ON QUIZZLER APP

import requests , html
from tkinter import *


THEME_COLOR = "#375362"

score = 0
count = 0
answer = None
quiz_ques = None
correct_answer = None


response = requests.get("https://opentdb.com/api.php?amount=10&type=boolean")
response.raise_for_status()

quiz_data = response.json()
question_data = quiz_data["results"]


def true():
    global answer
    answer = "True"
    feedback()


def false():
    global answer
    answer = "False"
    feedback()

def feedback():
    global score

    if answer == correct_answer:
        score +=1
        canvas.config(bg="green")

    else:
        canvas.config(bg="red")
    
    window.after(1000 , next_question)


def next_question():
    global count , quiz_ques , correct_answer
    count += 1

    canvas.config(bg="white")
    score_label.config(text=f"SCORE : {score}")

    if count <= 10 :
        quiz_ques = html.unescape(f"Q{count}. {question_data[count-1]['question']} (True/False)")
        correct_answer = question_data[count-1]["correct_answer"]
        canvas.itemconfig(quiz_text , text=quiz_ques)
    else:
        canvas.itemconfig(quiz_text, text="THE END")
        true_button.config(state="disabled")
        false_button.config(state="disabled")


# ------------------- UI SETUP ---------------------------------#

window = Tk()
window.title("QUIZZLER APP")
window.config(padx=50, pady=30 , bg=THEME_COLOR)

score_label = Label(text = f"SCORE : {score}" , fg="white" , bg=THEME_COLOR , font=("Cambria" , 30 , "bold") )
score_label.grid(row=0 , column=1 , columnspan=2)

canvas = Canvas(width=300 , height=300 , highlightthickness=0 , bg="white")
canvas.grid(row=1 , column=1 , columnspan=2 , pady= 30)
quiz_text = canvas.create_text(150 , 150 , text="STATRING QUIZ" , fill="black" , font=("Calibri" , 20 , "bold") , width=280)

true_img = PhotoImage(file="C:/Users/Mayank Aggarwal/Software Development/MAYANK/PYTHON PROGRAMMING/API/QUIZZLER APP/images/true.png")
false_img = PhotoImage(file="C:/Users/Mayank Aggarwal/Software Development/MAYANK/PYTHON PROGRAMMING/API/QUIZZLER APP/images/false.png")

true_button = Button(image=true_img , highlightthickness=0 , command=true , bd=5)
false_button = Button(image=false_img , highlightthickness=0 , command=false , bd=5)

true_button.grid(row=2 , column=2)
false_button.grid(row=2 ,column=1)

window.after(1000 , next_question)

window.mainloop()