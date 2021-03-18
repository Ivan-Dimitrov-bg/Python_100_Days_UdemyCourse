from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class QuizInterface():
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title = "Quiz APP"
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Question",
            fill=THEME_COLOR,
            font=("Ariel", 20, "italic"))
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
        self.score_label = Label(text=f"Score: {self.quiz.score}", bg=THEME_COLOR, fg="white", font=("Ariel", 20, "bold"))
        self.score_label.grid(column=1, row=0)

        self.get_next_question()
        image_right = PhotoImage(file="images/true.png")
        self.button_right = Button(image=image_right, command=self.true_is_clicked, highlightthickness=0)
        self.button_right.grid(column=0, row=2)

        image_wrong = PhotoImage(file="images/false.png")
        self.button_wrong = Button(image=image_wrong, command=self.false_is_clicked, highlightthickness=0)
        self.button_wrong.grid(column=1, row=2)



        self.canvas.mainloop()

    def true_is_clicked(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_is_clicked(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.get_next_question)

    def update_score(self):
        self.score_label.config(text=f"Score: {self.quiz.score}")

    def get_next_question(self):
        self.canvas.config(bg="white")
        self.update_score()
        if self.quiz.still_has_questions():
           q_text = self.quiz.next_question()
           self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz")
            self.button_right.config(state="disable")
            self.button_wrong.config(state="disable")
