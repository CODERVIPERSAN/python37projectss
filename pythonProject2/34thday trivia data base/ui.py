from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

# if object quiz is passed as the parameter
# please notify the datatype if not then there will be the error
class QuizInterface(Tk):
    def __init__(self,quiz:QuizBrain):
        super().__init__()
        self.quiz = quiz
        self.response = 0
        self.canvas = None
        # question and answer to be displayed
        self.question ='this is the question'
        self.answer ='false'
        # self.front_end()
        self.title(string="quizller")
        self.config(bg=THEME_COLOR, padx=20, pady=20)

        self.label = Label(text=f"Score{self.quiz.score}", font=("Arial", 10, "bold"))

        self.label.grid(row=0,column=5)
        self.canvas = Canvas(width=800, height=600, bg='white')
        self.question_txt = self.canvas.create_text(400, 300, text=self.question)
        self.canvas.itemconfig(self.question_txt, fill='black',font=('Arial',15,'normal'),width=780)
        self.canvas.grid(row=0, column=0, columnspan=2)

        right = PhotoImage(file='images/true.png')
        false = PhotoImage(file='images/false.png')

        self.right_button = Button(image=right, highlightthickness=0,command=self.right)
        self.wrong_button = Button(image=false, highlightthickness=0,command=self.wrong)

        self.right_button.grid(row=1, column=0)
        self.wrong_button.grid(row=1, column=1)
        self.get_next_question()
        self.mainloop()

    def get_next_question(self):
        self.refresh()
        if self.quiz.still_has_questions():
            self.question = self.quiz.next_question()
            self.canvas.itemconfig(self.question_txt,text=self.question)
            self.label.config(text=f"Score:{self.quiz.score}")
        else:
            self.canvas.itemconfig(self.question_txt,text="you reached the end of the quiz")
            self.right_button.config(state="disabled")
            self.wrong_button.config(state="disabled")
    def right(self):
        self.response ='true'
        is_right = self.quiz.check_answer(self.response)
        self.give_feedback(is_right)
    def wrong(self):
        self.response = 'false'
        is_right = self.quiz.check_answer(self.response)
        self.give_feedback(is_right)
    def give_feedback(self,is_right:bool)->bool:
        print(is_right)
        if is_right:
           self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')

        self.count_down(2)


    def count_down(self,n):
        if n!=0:
            self.after(1000,self.count_down,n-1)
        else:
            self.refresh()

            self.get_next_question()



    def crt_answer_color(self):
        self.canvas.config(bg="green")
    #
    def wrong_answer_color(self):
        self.canvas.config(bg="red")
    #
    def refresh(self):
        self.canvas.config(bg='white')
    # def checking(self):
    #     if self.response == self.answer:
    #         self.crt_answer_color()
    #     else:
    #         self.wrong_answer_color()
    #
    # def true(self):
    #     self.response ='true'
    #     self.checking()
    #
    # def false(self):
    #     self.response ='false'
    #     self.checking()


    # def front_end(self):








