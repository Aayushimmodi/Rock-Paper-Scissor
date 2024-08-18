from tkinter import *
import random
import  tkinter as tk

root = tk.Tk()

root.title("Rock, Paper, Scissor Game")
width = 600
height = 630
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(0, 0)


img = PhotoImage(file="images/pic.png")
label = Label(
    root,
    image=img
)
label.place(x=0, y=0)


result = StringVar()
score_com = IntVar()
score_you = IntVar()


blank_img=PhotoImage(file="images/blank.png")
player_rock=PhotoImage(file="images/player_rock.png")
sm_player_rock=player_rock.subsample(3, 3)
player_paper=PhotoImage(file="images/player_paper.png")
sm_player_paper=player_paper.subsample(3, 3)
player_scissor=PhotoImage(file="images/player_scissor.png")
sm_player_scissor= player_scissor.subsample(3, 3)
com_rock=PhotoImage(file="images/com_rock.png")
com_paper=PhotoImage(file="images/com_paper.png")
com_scissor=PhotoImage(file="images/com_scissor.png")



def draw(x):
    out = x  # Its a Draw"
    return result.set(out)


def player_win(x):
    out = x  # You Won"
    result.set(out)
    return score_you.set(score_you.get()+ 1)


def computer_wins(x):
    out = x  # 1 #     You Lost"
    result.set(out)
    return score_com.set(score_com.get()+ 1)


def Rock():
    global player_choice
    player_choice = 1
    player_img.configure(image=player_rock)
    MatchProcess()


def Paper():
    global player_choice
    player_choice = 2
    player_img.configure(image=player_paper)
    MatchProcess()


def Scissor():
    global player_choice
    player_choice = 3
    player_img.configure(image=player_scissor)
    MatchProcess()


def MatchProcess():
    com_choice = random.randint(1, 3)
    if com_choice == 1:
        comp_img.configure(image=com_rock)
        ComputerRock()
    elif com_choice == 2:
        comp_img.configure(image=com_paper)
        ComputerPaper()

    elif com_choice == 3:
        comp_img.configure(image=com_scissor)
        CompututerScissor()


def ComputerRock():
    if player_choice == 1:
        lbl_status.config(text="Game Tie")
        draw(1)
    elif player_choice == 2:
        lbl_status.config(text="Player Win")
        player_win(1)
    elif player_choice == 3:
        lbl_status.config(text="Computer Win")
        computer_wins(1)


def ComputerPaper():
    if player_choice == 1:
        lbl_status.config(text="Computer Win")
        computer_wins(1)
    elif player_choice == 2:
        lbl_status.config(text="Game Tie")
        draw(1)
    elif player_choice == 3:
        lbl_status.config(text="Player Win")
        player_win(1)


def CompututerScissor():
    if player_choice == 1:
        lbl_status.config(text="Player Win")
        player_win(1)
    elif player_choice == 2:
        lbl_status.config(text="Computer Win")
        computer_wins(1)
    elif player_choice == 3:
        lbl_status.config(text="Game Tie")
        draw(1)


def ExitApp():
    root.destroy()
    exit()


player_img = Label(root,image=blank_img)
comp_img = Label(root,image=blank_img)
lbl_player = Label(root,text="PLAYER")
lbl_player.grid(row=1, column=1)
lbl_player.config(bg="#99ff99")
lbl_computer = Label(root,text="COMPUTER")
lbl_computer.grid(row=1, column=3)
lbl_computer.config(bg="#99ff99")
lbl_status=Label(root, text="", font=('arial', 8))
lbl_status.config(bg="#99ff99")
player_img.grid(row=2,column=1, padx=30, pady=20)
comp_img.grid(row=2,column=3, pady=20)
lbl_status.grid(row=3, column=2)


ent1 = Entry(root, textvariable=result, width=27, font=('Ubuntu', 24), relief=GROOVE)


ent2 = Entry(root, textvariable=score_you, width=2, font=('Ubuntu', 24), relief=GROOVE)
ent2.place(relx=0.3, rely=0.85, anchor=CENTER)


msg2 = Label(root,text=' You ', font=("Courier", 8), relief=GROOVE)
msg2.place(relx=0.3, rely=0.79, anchor=CENTER)

msg3 = Label(root, text=' Com ', font=("Courier", 8), relief=GROOVE)
msg3.place(relx=0.7, rely=0.79, anchor=CENTER)




rock = Button(root, image=sm_player_rock, command=Rock)
rock.place(relx=0.7, rely=0.79, anchor=CENTER)
paper = Button(root, image=sm_player_paper, command=Paper)
scissor = Button(root, image=sm_player_scissor, command=Scissor)

rock.grid(row=4,column=1, pady=30)
paper.grid(row=4,column=2, pady=30)
scissor.grid(row=4,column=3, pady=30)


msg4 = Label(root, text=' Score Board ', font=("Courier", 18), relief=GROOVE)
msg4.place(relx=0.5, rely=0.85, anchor=CENTER)

ent3 = Entry(root, textvariable=score_com, width=2,
             font=('Ubuntu', 24), relief=GROOVE)
ent3.place(relx=0.7, rely=0.85, anchor=CENTER)


btn_quit = Button(root, text='QUIT', width=91, command=root.destroy,
                 bg="red", activebackground="red", relief=GROOVE)
btn_quit.place(relx=0.5, rely=1, anchor=S)



if __name__ == '__main__':
 root.mainloop()


