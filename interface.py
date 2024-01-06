class advanced_interface:
    def make_btn(self, a, b, func):

        b[a[0]] = self.tk.Button(background="#FCA311", foreground="#14213D", text=a[0], height=5, width=10,
                                    master=self.frame2,
                                    command=lambda: func(a[0]))
        b[a[0]].bind("<Enter>", lambda event: self.show_short(event, a[1], a[2], a[3]))
        b[a[0]].bind("<Leave>", lambda event: self.last_short.destroy())
        b[a[0]].grid(column=a[2], row=a[3])
        if func == self.new_input:
            self.window.bind(a[0], lambda event: func(a[0]))
        return b


    def btns(self):
        b = {}
        text = ""
        with open("texts/abtn.txt", "r")as file:
            text = (file.read())
        s = text.split("\n")
        f = []
        for m in s:
            temp = m.split(" ")
            f.append([str(temp[0]), str(temp[1]), int(temp[2]), int(temp[3])])

        for a in f:
            b = self.make_btn(a, b, self.new_input)
        #_________________________________________
        texts = ""
        with open("texts/asbtns.txt", "r") as file:
            texts = (file.read())
        s = texts.split("\n")
        f = []
        for m in s:
            temp = m.split(" ")
            f.append([str(temp[0]), str(temp[1]), int(temp[2]), int(temp[3])])
        funs = {"mem": self.ev_mem, "mod": self.ev_change_mode,"MRC": self.ev_MRC,
                "Ans": self.ev_ans, "=": self.ev_equal}

        for a in f:
            b = self.make_btn(a, b, funs[a[0]])


    def document(self):
        nwindow = self.tk.Tk()
        nwindow.title("document")

        label = self.tk.Label(text=self.doc, background="cyan", master=nwindow)
        label.grid(column=0, row=0)
        label1 = self.tk.Label(text=self.doc2, background="lightblue", master=nwindow)
        label1.grid(column=1, row=0)
        nwindow.update()

    def show_short(self, event, text, collumn, row):
        self.last_short = self.tk.Toplevel()
        self.last_short.overrideredirect(True)
        self.last_short.geometry("+{}+{}".format(20 + self.x+(collumn*85), 180 + self.y+(row*85)))
        shortcut_label = self.tk.Label(self.last_short, text=text, background="yellow")
        shortcut_label.pack()
    def binds(self):
        self.window.bind('s', lambda event: self.new_input("s"))
        self.window.bind('i', lambda event: self.new_input("i"))
        self.window.bind('n', lambda event: self.new_input("n"))
        self.window.bind('a', lambda event: self.new_input("a"))
        self.window.bind('t', lambda event: self.new_input("t"))
        self.window.bind('c', lambda event: self.new_input("c"))
        self.window.bind('o', lambda event: self.new_input("o"))
        self.window.bind('l', lambda event: self.new_input("l"))
        self.window.bind('g', lambda event: self.new_input("g"))
        self.window.bind('e', lambda event: quit())
        self.window.bind('q', lambda event: quit())
        self.window.bind('=', lambda event: self.ev_equal())
        self.window.bind('<Return>', lambda event: self.ev_equal())
        self.window.bind('<BackSpace>', lambda event: self.ev_DEL())
        self.window.bind('<Escape>', lambda event: self.ev_AC())
        self.window.bind('<Tab>', lambda event: self.ev_change_mode())
        self.window.bind('<space>', lambda event: self.ev_mem())
        self.window.bind('@', lambda event: self.ev_ans())
        self.window.bind('r', lambda event: self.ev_AR())


    def gem(self):
        geometry_temp = self.utility.input_to_list.action("sin", "+-x", self.window.geometry())
        self.x = int(geometry_temp[4])
        self.y = int(geometry_temp[6])


    def __init__(self, num=0, memorylist=[], opnum=0):
        import tkinter as tk
        import calculator, utility
        self.tk = tk
        self.calculator = calculator
        self.utility = utility
        if num == 0:
            self.window = tk.Tk()
            self.window.geometry("+{}+{}".format(100, 100))
            self.window.bind("<Configure>", lambda event: self.gem())
        self.gem()
        self.is_seen = False
        self.memory_list = memorylist
        self.backward = 0
        self.opnum = opnum
        self.mm = 0
        self.last_short = None
        self.doc = "button    \n" \
                   "_____________\n" \
                   "numbers     \n" \
                   "parenthese  \n" \
                   "operations  \n" \
                   "mem         \n" \
                   "Ac         \n" \
                   "DEL        \n" \
                   "exit      \n" \
                   "equal or =  \n" \
                   "mod         \n" \
                   "Ans         \n" \
                   "sin,cos,...\n" \
                   "Autoreply\n" \
                   "MRC\n" \
                   "!!"
        self.doc2 = "shortcut key\n" \
                    "_____________\n" \
                    "numbers\n" \
                    "parentheses\n" \
                    "operations\n" \
                    "Space\n" \
                    "Escape/ Esc\n" \
                    "Backspace\n" \
                    "e or q\n" \
                    "Enter or =\n" \
                    "Tab\n" \
                    "@\n" \
                    "t,a,n,c,o,s,i,l,g\n" \
                    "r\n" \
                    "m\n" \
                    "!"
        self.binds()
        self.window.title('Calculator')
        menubar = self.tk.Menu(self.window)
        self.window.config(menu=menubar)
        file_menu = self.tk.Menu(menubar)
        file_menu.add_command(
            label='keyboard_buttons',
            command=self.document
        )
        menubar.add_cascade(
            label="document",
            menu=file_menu
        )
        # frames
        frame1 = tk.Frame()
        frame1.pack(fill=tk.X)
        self.frame2 = tk.Frame()
        self.frame2.pack()
        # labels
        self.label = tk.Label(background="lightgray", height=3, master=frame1)
        self.label.pack(fill=tk.X)
        self.label2 = tk.Label(background="#4F6467", foreground="white", height=1, master=frame1)
        self.label2.pack(fill=tk.X)
        self.label3 = tk.Label(text="you had done nothing yet", background="lightgreen", foreground="black",
                               master=self.frame2, wraplength=100)
        self.label3.grid(column=7, row=2, sticky="nswe")
        self.label4 = tk.Label(text=".........", background="lightgreen", foreground="black",
                               master=self.frame2, wraplength=100)
        self.label4.grid(column=7, row=3, sticky="nswe")
        self.label5 = tk.Label(text=".........", background="lightgreen", foreground="black",
                               master=self.frame2, wraplength=100)
        self.label5.grid(column=7, row=4, sticky="nswe")
        # buttons
        btn_list = self.btns()
        btn_DEL = tk.Button(background="#FCA311", foreground="#14213D", text="DEL", height=5, width=20, master=self.frame2,
                            command=self.ev_DEL)
        btn_DEL.bind("<Enter>", lambda event: self.show_short(event, "Backspace", 7, 1))
        btn_DEL.bind("<Leave>", lambda event: self.last_short.destroy())
        btn_AC = tk.Button(background="#FCA311", foreground="#14213D", text="AC", height=5, width=20, master=self.frame2,
                           command=self.ev_AC)
        btn_AC.bind("<Enter>", lambda event: self.show_short(event, "Esc", 7, 0))
        btn_AC.bind("<Leave>", lambda event: self.last_short.destroy())
        btn_00 = tk.Button(background="#FCA311", foreground="#14213D", text="00", height=5, width=10,
                            master=self.frame2, command=self.ev_00)
        btn_auto_r = tk.Button(background="#FCA311", foreground="#14213D", text="Auto\nreply", height=5, width=10,
                            master=self.frame2, command=self.ev_AR)
        btn_auto_r.bind("<Enter>", lambda event: self.show_short(event, "r", 0, 0))
        btn_auto_r.bind("<Leave>", lambda event: self.last_short.destroy())
        btn_Mp = tk.Button(background="#FCA311", foreground="#14213D", text="M+", height=5, width=10,
                            master=self.frame2, command=self.ev_Mp)
        btn_Mm = tk.Button(background="#FCA311", foreground="#14213D", text="M-", height=5, width=10,
                            master=self.frame2, command=self.ev_Mm)
        btn_Mp.grid(column=0, row=2)
        btn_Mm.grid(column=0, row=3)
        btn_auto_r.grid(column=0, row=0)
        btn_00.grid(column=0, row=4)
        btn_DEL.grid(column=7, row=1)
        btn_AC.grid(column=7, row=0)
        if self.memory_list:
            self.label3.config(text=f"here; {str(len(self.memory_list))} problems have been solved")
        if self.opnum:
            self.label4.config(text=f"in last problem you used {self.opnum} functions and operations")
        self.window.mainloop()

    def new_input(self, inp):
        if inp in "+-/*^%sincostancotlogln!!":
            self.opnum += 1


        if self.is_seen:
            self.label.config(text="")
            self.is_seen = False
        last_text = self.label["text"]
        self.label.config(text=last_text+inp)

    def ev_0(self):
        self.new_input("0")

    def ev_1(self):
        self.new_input("1")

    def ev_2(self):
        self.new_input("2")

    def ev_3(self):
        self.new_input("3")

    def ev_4(self):
        self.new_input("4")

    def ev_5(self):
        self.new_input("5")

    def ev_6(self):
        self.new_input("6")

    def ev_7(self):
        self.new_input("7")

    def ev_8(self):
        self.new_input("8")

    def ev_9(self):
        self.new_input("9")

    def ev_00(self):
        self.new_input("00")

    def ev_plus(self):
        self.new_input("+")

    def ev_minus(self):
        self.new_input("-")

    def ev_multiple(self):
        self.new_input("*")

    def ev_divide(self):
        self.new_input("/")

    def ev_ashar(self):
        self.new_input(".")

    def ev_equal(self):
        try:
            self.label2.config(text=self.calculator.Calculator.calculate(self.utility.input_checker.action(self.label["text"])))
            self.memory_list.append((self.label["text"], self.label2["text"]))
            self.label3.config(text=f"here; {str(len(self.memory_list))} problems have been solved")
            self.label4.config(text=f"in last problem you used {self.opnum} functions and operations")
            self.label5.config(text=".........", background="lightgreen", foreground="black")
        except:
            self.label5.config(text="wrong syntax!", background="red", foreground="blue")
        self.is_seen = True
        self.backward = 0
        self.opnum = 0

    def ev_power(self):
        self.new_input("^")

    def ev_remaining(self):
        self.new_input("%")

    def ev_parentheses_start(self):
        self.new_input("(")

    def ev_parentheses_end(self):
        self.new_input(")")

    def ev_change_mode(self, num=0):
        global simple_interface
        if num == 0:
            self.window.destroy()
            a = simple_interface(memorylist=self.memory_list, opnum=self.opnum)
        else:
            a = simple_interface(memorylist=self.memory_list, opnum=self.opnum)
            return a.window

    def ev_AC(self):
        self.label.config(text="")
        self.label2.config(text="")
        self.opnum = 0
        self.memory_list = []
        self.label3.config(text="you had done nothing yet")
        self.label4.config(text=".........")

    def ev_DEL(self):
        self.label.config(text=self.label["text"][0:len(self.label["text"])-1])

    def ev_mem(self):
        self.backward += 1
        try:
            a = self.memory_list[len(self.memory_list)-1-self.backward]
            self.label.config(text=a[0])
            self.label2.config(text=a[1])
        except:
            pass

    def ev_ans(self):
        self.new_input(str(self.memory_list[len(self.memory_list)-1-self.backward][1]))

    def ev_ft(self):
        self.new_input("!!")

    def ev_sin(self):
        self.new_input("sin")

    def ev_cos(self):
        self.new_input("cos")

    def ev_tan(self):
        self.new_input("tan")

    def ev_cot(self):
        self.new_input("cot")

    def ev_log(self):
        self.new_input("log")

    def ev_ln(self):
        self.new_input("ln")

    def ev_MRC(self):
        self.new_input(str(self.mm))

    def ev_Mp(self):
        self.mm = float(self.label2["text"])

    def ev_Mm(self):
        self.mm = -float(self.label2["text"])

    def ev_AR(self):
        for a in self.memory_list:
            self.label.config(text=a[0])
            self.label2.config(text=a[1])
            self.window.update()
            from time import sleep as sl
            sl(1)






class simple_interface:

    def make_btn(self, a, b, func):

        b[a[0]] = self.tk.Button(background="#FCA311", foreground="#14213D", text=a[0], height=5, width=10,
                                    master=self.frame2,
                                    command=lambda: func(a[0]))
        b[a[0]].bind("<Enter>", lambda event: self.show_short(event, a[1], a[2], a[3]))
        b[a[0]].bind("<Leave>", lambda event: self.last_short.destroy())
        b[a[0]].grid(column=a[2], row=a[3])
        if func == self.new_input:
            self.window.bind(a[0], lambda event: func(a[0]))
        return b


    def btns(self):
        b = {}
        text = ""
        with open("texts/btn.txt", "r")as file:
            text = (file.read())
        s = text.split("\n")
        f = []
        for m in s:
            temp = m.split(" ")
            f.append([str(temp[0]), str(temp[1]), int(temp[2]), int(temp[3])])

        for a in f:
            b = self.make_btn(a, b, self.new_input)
        #_________________________________________
        texts = ""
        with open("texts/sbtns.txt", "r") as file:
            texts = (file.read())
        s = texts.split("\n")
        f = []
        for m in s:
            temp = m.split(" ")
            f.append([str(temp[0]), str(temp[1]), int(temp[2]), int(temp[3])])
        funs = {"mem": self.ev_mem, "mod": self.ev_change_mode, "DEL": self.ev_DEL, "AC": self.ev_AC,
                "Ans": self.ev_ans, "=": self.ev_equal}

        for a in f:
            b = self.make_btn(a, b, funs[a[0]])


    def show_short(self, event, text, collumn, row):
        self.last_short = self.tk.Toplevel()
        self.last_short.overrideredirect(True)
        self.last_short.geometry("+{}+{}".format(10 + self.x+(collumn*85), 180 + self.y+(row*85)))
        shortcut_label = self.tk.Label(self.last_short, text=text, background="yellow")
        shortcut_label.pack()

    def binds(self):
        self.window.bind('q', lambda event: quit())
        self.window.bind('e', lambda event: quit())
        self.window.bind('=', lambda event: self.ev_equal())
        self.window.bind('<Return>', lambda event: self.ev_equal())
        self.window.bind('<BackSpace>', lambda event: self.ev_DEL())
        self.window.bind('<Escape>', lambda event: self.ev_AC())
        self.window.bind('<Tab>', lambda event: self.ev_change_mode())
        self.window.bind('<space>', lambda event: self.ev_mem())
        self.window.bind('@', lambda event: self.ev_ans())


    def document(self):
        nwindow = self.tk.Tk()
        nwindow.title("document")

        label = self.tk.Label(text=self.doc, background="cyan", master=nwindow)
        label.grid(column=0, row=0)
        label1 = self.tk.Label(text=self.doc2, background="lightblue", master=nwindow)
        label1.grid(column=1, row=0)
        nwindow.update()

    def gem(self):
        geometry_temp = self.utility.input_to_list.action("sin", "+-x", self.window.geometry())
        self.x = int(geometry_temp[4])
        self.y = int(geometry_temp[6])

    def __init__(self, memorylist=[], opnum=0):
        import tkinter as tk
        import calculator, utility
        self.tk = tk
        self.last_short = None
        self.calculator = calculator
        self.utility = utility
        self.window = tk.Tk()
        self.is_seen = False
        self.memory_list = memorylist
        self.backward = 0
        self.opnum = opnum
        self.window.geometry("+{}+{}".format(100, 100))
        self.window.bind("<Configure>", lambda event: self.gem())
        self.gem()
        self.binds()
        self.window.title("Calculator")
        self.doc = "button    \n" \
                   "_____________\n" \
                   "numbers     \n" \
                   "parenthese  \n" \
                   "operations  \n" \
                   "mem         \n" \
                   "Ac         \n" \
                   "DEL        \n" \
                   "exit      \n" \
                   "equal or =  \n" \
                   "mod         \n" \
                   "Ans         "
        self.doc2 = "shortcut key\n" \
                    "_____________\n" \
                    "numbers\n" \
                    "parentheses\n" \
                    "operations\n" \
                    "Space\n" \
                    "Escape/ Esc\n" \
                    "Backspace\n" \
                    "e or q\n" \
                    "Enter or =\n" \
                    "Tab\n" \
                    "@"
        menubar = self.tk.Menu(self.window)
        self.window.config(menu=menubar)
        # create a menu
        file_menu = self.tk.Menu(menubar)
        # add a menu item to the menu
        file_menu.add_command(
            label='keyboard_buttons',
            command=self.document
        )
        # add the File menu to the menubar
        menubar.add_cascade(
            label="document",
            menu=file_menu
        )
        # frames
        frame1 = tk.Frame()
        frame1.pack(fill=tk.X)
        self.frame2 = tk.Frame()
        self.frame2.pack()
        # inputed label
        self.label = tk.Label(background="lightgray", height=3, master=frame1)
        self.label.pack(fill=tk.X)
        self.label2 = tk.Label(background="#4F6467", foreground="white", height=1, master=frame1)
        self.label2.pack(fill=tk.X)
        # buttons
        btn_list = self.btns()

        self.window.mainloop()

    def new_input(self, inp):
        if inp in "+-/*^%sincostancotlogln!!":
            self.opnum += 1

        if self.is_seen:
            self.label.config(text="")
            self.is_seen = False
        last_text = self.label["text"]
        self.label.config(text=last_text+inp)

    def ev_equal(self, temp=None):
        try:
            self.label2.config(text=self.calculator.Calculator.calculate(self.utility.input_checker.action(self.label["text"])))
            self.memory_list.append((self.label["text"], self.label2["text"]))
        except:

            self.window.destroy()
            a = self.tk.Tk()
            b = self.tk.Label(text="wrong syntax!!!",font=("", 20), background="red", foreground="blue", master=a)
            b.pack(fill="both")
            a.mainloop()

            global advanced_interface
            n = advanced_interface(1)

            self.window = n.ev_change_mode(1)
        self.is_seen = True
        self.backward = 0

    def ev_change_mode(self, temp=None):
        self.window.destroy()
        global advanced_interface
        b = advanced_interface(memorylist=self.memory_list, opnum=self.opnum)

    def ev_AC(self, temp=None):
        self.label.config(text="")
        self.label2.config(text="")
        self.memory_list = []
        self.opnum = 0

    def ev_DEL(self, temp=None):
        self.label.config(text=self.label["text"][0:len(self.label["text"])-1])

    def ev_mem(self, temp=None):
        self.backward += 1
        try:
            a = self.memory_list[len(self.memory_list)-1-self.backward]
            self.label.config(text=a[0])
            self.label2.config(text=a[1])
        except:
            pass

    def ev_ans(self, temp=None):
        self.new_input(str(self.memory_list[len(self.memory_list)-1-self.backward][1]))


a = simple_interface()
