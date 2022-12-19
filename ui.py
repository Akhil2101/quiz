from tkinter import *


class GraphicInterface:
    def __init__(self,quiz_brain):
        self.quiz=quiz_brain
        self.window=Tk()
        self.window.title("quizzer")
        self.window.config(padx=20,pady=20,bg='#375362')
        self.score_label=Label(text="Score:0",highlightthickness=0,bg='#375362',fg='white')
        self.score_label.grid(row=0,column=1)
        self.canvas=Canvas(width=300,height=250,highlightthickness=0)
        self.quiz_text=self.canvas.create_text(150,125,width=280,text="welcome here to quiz",font=('arial',20,'italic'))
        self.canvas.grid(row=1,column=0,columnspan=2,pady=50)
        image_right=PhotoImage(file="right.png")
        image_left=PhotoImage(file="wrong.png")
        self.right_button=Button(image=image_right,command=self.right_pressed)
        self.right_button.grid(row=2,column=0)
        self.left_button = Button(image=image_left,command=self.left_pressed)
        self.left_button.grid(row=2, column=1)
        self.next_ui()
        self.window.mainloop()
    def next_ui(self):
        self.canvas.config(bg="white")
        set_ques=self.quiz.next_question()
        self.canvas.itemconfig(self.quiz_text,text=set_ques)
    def right_pressed(self):
        answer=self.quiz.check_answer("true")
        self.final_gui(answer)

    def left_pressed(self):
        answer=self.quiz.check_answer("false")
        self.final_gui(answer)
    def final_gui(self,answer):
        if answer:
            self.canvas.config(bg="green")
            self.score_label.config(text=f"score:{self.quiz.score}")
            self.window.after(1000,self.next_ui)
        else:
            self.canvas.config(bg="red")
            self.window.after(1000, self.next_ui)



