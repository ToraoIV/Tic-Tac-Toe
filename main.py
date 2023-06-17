import customtkinter as ctk

root = ctk.CTk()
root.title("TicTacToe")
root.geometry("300x350")
root.resizable(False, False)

frame = ctk.CTkFrame(root, width=300, height=50, corner_radius=0, fg_color="transparent")
frame.place(x=0, y=0)

frame1 = ctk.CTkFrame(root, width=300, height=300, corner_radius=0, fg_color="#bababa")
frame1.place(x=0, y=50)

label = ctk.CTkLabel(frame, text="Tic-Tac-Toe", font=("Noto Sans CJK JP", 25, "bold"))
label.place(x=150, y=25, anchor="center")

button1 = ctk.CTkButton(frame1, text="", width=100, height=100, corner_radius=0, fg_color="#242424", font=("Noto Sans CJK JP", 30, "bold"), hover_color="#404040", state="normal", command=lambda: dene(button1))
button2 = ctk.CTkButton(frame1, text="", width=100, height=100, corner_radius=0, fg_color="#242424", font=("Noto Sans CJK JP", 30, "bold"), hover_color="#404040", state="normal", command=lambda: dene(button2))
button3 = ctk.CTkButton(frame1, text="", width=100, height=100, corner_radius=0, fg_color="#242424", font=("Noto Sans CJK JP", 30, "bold"), hover_color="#404040", state="normal", command=lambda: dene(button3))

button4 = ctk.CTkButton(frame1, text="", width=100, height=100, corner_radius=0, fg_color="#242424", font=("Noto Sans CJK JP", 30, "bold"), hover_color="#404040", state="normal", command=lambda: dene(button4))
button5 = ctk.CTkButton(frame1, text="", width=100, height=100, corner_radius=0, fg_color="#242424", font=("Noto Sans CJK JP", 30, "bold"), hover_color="#404040", state="normal", command=lambda: dene(button5))
button6 = ctk.CTkButton(frame1, text="", width=100, height=100, corner_radius=0, fg_color="#242424", font=("Noto Sans CJK JP", 30, "bold"), hover_color="#404040", state="normal", command=lambda: dene(button6))

button7 = ctk.CTkButton(frame1, text="", width=100, height=100, corner_radius=0, fg_color="#242424", font=("Noto Sans CJK JP", 30, "bold"), hover_color="#404040", state="normal", command=lambda: dene(button7))
button8 = ctk.CTkButton(frame1, text="", width=100, height=100, corner_radius=0, fg_color="#242424", font=("Noto Sans CJK JP", 30, "bold"), hover_color="#404040", state="normal", command=lambda: dene(button8))
button9 = ctk.CTkButton(frame1, text="", width=100, height=100, corner_radius=0, fg_color="#242424", font=("Noto Sans CJK JP", 30, "bold"), hover_color="#404040", state="normal", command=lambda: dene(button9))

button1.place(x=0, y=0)
button2.place(x=103, y=0)
button3.place(x=206, y=0)

button4.place(x=0, y=103)
button5.place(x=103, y=103)
button6.place(x=206, y=103)

button7.place(x=0, y=206)
button8.place(x=103, y=206)
button9.place(x=206, y=206)

count = 9
turn = True
win = False

buttons = [button1, button2, button3, button4, button5, button6, button7, button8, button9]


def check_win():
    global win
    if (button1.cget("text") == button2.cget("text") == button3.cget("text")) and (button1.cget("text") != ""):
        win = True
        if turn:
            for a in (button1, button2, button3):
                a.configure(text_color_disabled="red")
        else:
            for a in (button1, button2, button3):
                a.configure(text_color_disabled="green")
    elif (button4.cget("text") == button5.cget("text") == button6.cget("text")) and (button4.cget("text") != ""):
        win = True
        if turn:
            for a in (button4, button5, button6):
                a.configure(text_color_disabled="red")
        else:
            for a in (button4, button5, button6):
                a.configure(text_color_disabled="green")
    elif (button7.cget("text") == button8.cget("text") == button9.cget("text")) and (button7.cget("text") != ""):
        win = True
        if turn:
            for a in (button7, button8, button9):
                a.configure(text_color_disabled="red")
        else:
            for a in (button7, button8, button9):
                a.configure(text_color_disabled="green")
    elif (button1.cget("text") == button4.cget("text") == button7.cget("text")) and (button1.cget("text") != ""):
        win = True
        if turn:
            for a in (button1, button4, button7):
                a.configure(text_color_disabled="red")
        else:
            for a in (button1, button4, button7):
                a.configure(text_color_disabled="green")
    elif (button2.cget("text") == button5.cget("text") == button8.cget("text")) and (button2.cget("text") != ""):
        win = True
        if turn:
            for a in (button2, button5, button8):
                a.configure(text_color_disabled="red")
        else:
            for a in (button2, button5, button8):
                a.configure(text_color_disabled="green")
    elif (button3.cget("text") == button6.cget("text") == button9.cget("text")) and (button3.cget("text") != ""):
        win = True
        if turn:
            for a in (button3, button6, button9):
                a.configure(text_color_disabled="red")
        else:
            for a in (button3, button6, button9):
                a.configure(text_color_disabled="green")
    elif (button1.cget("text") == button5.cget("text") == button9.cget("text")) and (button1.cget("text") != ""):
        win = True
        if turn:
            button1.configure(text_color_disabled="red")
        else:
            button1.configure(text_color_disabled="green")
    elif (button3.cget("text") == button5.cget("text") == button7.cget("text")) and (button3.cget("text") != ""):
        win = True
        if turn:
            for a in (button3, button5, button7):
                a.configure(text_color_disabled="red")
        else:
            for a in (button3, button5, button7):
                a.configure(text_color_disabled="green")


def dene(b):
    global turn, count
    count -= 1
    b.configure(state="disabled")
    if turn:
        b.configure(text="X")
        turn = False
        label.configure(text="Player 2")
    else:
        b.configure(text="O")
        turn = True
        label.configure(text="Player 1")
    if count == 0:
        label.configure(text="Tie")
    check_win()
    if win:
        for x in list(buttons):
            x.configure(state="disabled")
        if turn:
            label.configure(text="Player 2 Win")
        else:
            label.configure(text="Player 1 Win")


root.mainloop()
