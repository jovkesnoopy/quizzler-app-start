from tkinter import *
from data import question_data
import random
import html
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.score = 0

        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text=html.unescape(random.choice(question_data)['question']),
            fill=THEME_COLOR,
            font=("Arial", 20, "italic")
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_img = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_img, highlightthickness=0, command=self.true_pressed)
        self.true_button.grid(row=2, column=0)

        false_img = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_img, highlightthickness=0, command=self.false_pressed)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
            self.canvas.itemconfig(self.question_text, fill=THEME_COLOR)
        else:
            self.canvas.itemconfig(self.question_text, text=f"You've completed the quiz!\n"
                                                            f"Your final score was: {self.score}/10",
                                                            fill=THEME_COLOR)
            self.canvas.config(bg="white")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    '''Create two new methods that you can add as a command to the buttons. 
    The methods need to call "check_answer()" from the quiz_brain and pass over the string "True" or "False".'''
    def true_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
            self.canvas.itemconfig(self.question_text, text="Correct", fill="white")
            self.score += 1
            self.score_label.config(text=f"Score: {self.score}")
        else:
            self.canvas.config(bg="red")
            self.canvas.itemconfig(self.question_text, text="Wrong", fill="white")
        self.window.after(1000, self.get_next_question)





