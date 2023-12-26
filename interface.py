import tkinter as tk
import calculator, utility
window = tk.Tk()

is_seen = False
memory_list = []
backward = 0

def new_input(inp):
    global is_seen
    if is_seen:
        label.config(text="")
        is_seen = False
    last_text = label["text"]
    label.config(text=last_text+inp)


def ev_0():
    new_input("0")


def ev_1():
    new_input("1")


def ev_2():
    new_input("2")


def ev_3():
    new_input("3")


def ev_4():
    new_input("4")


def ev_5():
    new_input("5")


def ev_6():
    new_input("6")


def ev_7():
    new_input("7")


def ev_8():
    new_input("8")


def ev_9():
    new_input("9")


def ev_plus():
    new_input("+")


def ev_minus():
    new_input("-")


def ev_multiple():
    new_input("*")


def ev_divide():
    new_input("/")


def ev_ashar():
    new_input(".")


def ev_equal():
    label2.config(text=calculator.Calculator.calculate(utility.input_checker.action(label["text"])))
    memory_list.append((label["text"], label2["text"]))
    global is_seen
    is_seen = True
    global backward
    backward = 0


def ev_power():
    new_input("^")


def ev_remaining():
    new_input("%")


def ev_parentheses_start():
    new_input("(")


def ev_parentheses_end():
    new_input(")")


def ev_change_mode():
    pass


def ev_AC():
    label.config(text="")
    label2.config(text="")


def ev_DEL():
    label.config(text=label["text"][0:len(label["text"])-1])


def ev_mem():
    global memory_list
    global backward
    backward += 1
    try:
        a = memory_list[len(memory_list)-1-backward]
        label.config(text=a[0])
        label2.config(text=a[1])
    except:
        pass

def ev_ans():
    global memory_list
    global backward
    new_input(str(memory_list[len(memory_list)-1-backward][1]))

# frames
frame1 = tk.Frame()
frame1.pack(fill=tk.X)

frame2 = tk.Frame()
frame2.pack()

# inputed label

label = tk.Label(background="lightgray", height=3, master=frame1)
label.pack(fill=tk.X)

label2 = tk.Label(background="#4F6467", foreground="white", height=1, master=frame1)
label2.pack(fill=tk.X)

# buttons
btn_0 = tk.Button(background="#FCA311", foreground="#14213D", text="0", height=5, width=10, master=frame2, command=ev_0)
btn_1 = tk.Button(background="#FCA311", foreground="#14213D", text="1", height=5, width=10, master=frame2, command=ev_1)
btn_2 = tk.Button(background="#FCA311", foreground="#14213D", text="2", height=5, width=10, master=frame2, command=ev_2)
btn_3 = tk.Button(background="#FCA311", foreground="#14213D", text="3", height=5, width=10, master=frame2, command=ev_3)
btn_4 = tk.Button(background="#FCA311", foreground="#14213D", text="4", height=5, width=10, master=frame2, command=ev_4)
btn_5 = tk.Button(background="#FCA311", foreground="#14213D", text="5", height=5, width=10, master=frame2, command=ev_5)
btn_6 = tk.Button(background="#FCA311", foreground="#14213D", text="6", height=5, width=10, master=frame2, command=ev_6)
btn_7 = tk.Button(background="#FCA311", foreground="#14213D", text="7", height=5, width=10, master=frame2, command=ev_7)
btn_8 = tk.Button(background="#FCA311", foreground="#14213D", text="8", height=5, width=10, master=frame2, command=ev_8)
btn_9 = tk.Button(background="#FCA311", foreground="#14213D", text="9", height=5, width=10, master=frame2, command=ev_9)

btn_plus = tk.Button(background="#FCA311", foreground="#14213D", text="+", height=5, width=10, master=frame2, command=ev_plus)
btn_minus = tk.Button(background="#FCA311", foreground="#14213D", text="-", height=5, width=10, master=frame2, command=ev_minus)
btn_multiple = tk.Button(background="#FCA311", foreground="#14213D", text="*", height=5, width=10, master=frame2, command=ev_multiple)
btn_divide = tk.Button(background="#FCA311", foreground="#14213D", text="/", height=5, width=10, master=frame2, command=ev_divide)
btn_equal = tk.Button(background="#FCA311", foreground="#14213D", text="=", height=5, width=10, master=frame2, command=ev_equal)
btn_ashar = tk.Button(background="#FCA311", foreground="#14213D", text=".", height=5, width=10, master=frame2, command=ev_ashar)


btn_parentheses_start = tk.Button(background="#FCA311", foreground="#14213D", text="(", height=5, width=10, master=frame2, command=ev_parentheses_start)
btn_remaining = tk.Button(background="#FCA311", foreground="#14213D", text="%", height=5, width=10, master=frame2, command=ev_remaining)
btn_last_answer = tk.Button(background="#FCA311", foreground="#14213D", text="Ans", height=5, width=10, master=frame2, command=ev_ans)
btn_DEL = tk.Button(background="#FCA311", foreground="#14213D", text="DEL", height=5, width=10, master=frame2, command=ev_DEL)
btn_AC = tk.Button(background="#FCA311", foreground="#14213D", text="AC", height=5, width=10, master=frame2, command=ev_AC)
btn_parentheses_end = tk.Button(background="#FCA311", foreground="#14213D", text=")", height=5, width=10, master=frame2, command=ev_parentheses_end)
btn_power = tk.Button(background="#FCA311", foreground="#14213D", text="^", height=5, width=10, master=frame2, command=ev_power)
btn_memory = tk.Button(background="#FCA311", foreground="#14213D", text="mem", height=5, width=10, master=frame2, command=ev_mem)
btn_change_mod = tk.Button(background="#FCA311", foreground="#14213D", text="EXP", height=5, width=10, master=frame2, command=ev_change_mode)





btn_power.grid(column=0, row=0)
btn_memory.grid(column=1, row=0)
btn_change_mod.grid(column=2, row=0)
btn_DEL.grid(column=3, row=0)
btn_AC.grid(column=4, row=0)
btn_parentheses_end.grid(column=4, row=1)
btn_parentheses_start.grid(column=3, row=1)
btn_remaining.grid(column=3, row=4)
btn_last_answer.grid(column=2, row=4)




btn_7.grid(column=0, row=1)
btn_8.grid(column=1, row=1)
btn_9.grid(column=2, row=1)
btn_4.grid(column=0, row=2)
btn_5.grid(column=1, row=2)
btn_6.grid(column=2, row=2)
btn_1.grid(column=0, row=3)
btn_2.grid(column=1, row=3)
btn_3.grid(column=2, row=3)
btn_0.grid(column=0, row=4)

btn_ashar.grid(column=1, row=4)
btn_equal.grid(column=4, row=4)
btn_plus.grid(column=3, row=3)
btn_minus.grid(column=4, row=3)
btn_multiple.grid(column=3, row=2)
btn_divide.grid(column=4, row=2)

























window.mainloop()
