class advanced_interface:


    def binds(self):

        self.window.bind('0', lambda event: self.ev_0())
        self.window.bind('1', lambda event: self.ev_1())
        self.window.bind('2', lambda event: self.ev_2())
        self.window.bind('3', lambda event: self.ev_3())
        self.window.bind('4', lambda event: self.ev_4())
        self.window.bind('5', lambda event: self.ev_5())
        self.window.bind('6', lambda event: self.ev_6())
        self.window.bind('7', lambda event: self.ev_7())
        self.window.bind('8', lambda event: self.ev_8())
        self.window.bind('9', lambda event: self.ev_9())
        self.window.bind('s', lambda event: self.new_input("s"))
        self.window.bind('i', lambda event: self.new_input("i"))
        self.window.bind('n', lambda event: self.new_input("n"))
        self.window.bind('a', lambda event: self.new_input("a"))
        self.window.bind('t', lambda event: self.new_input("t"))
        self.window.bind('c', lambda event: self.new_input("c"))
        self.window.bind('o', lambda event: self.new_input("o"))
        self.window.bind('l', lambda event: self.new_input("l"))
        self.window.bind('g', lambda event: self.new_input("g"))
        self.window.bind('!', lambda event: self.new_input("!!"))
        self.window.bind('.', lambda event: self.new_input("."))
        self.window.bind('+', lambda event: self.new_input("+"))
        self.window.bind('-', lambda event: self.new_input("-"))
        self.window.bind('/', lambda event: self.new_input("/"))
        self.window.bind('*', lambda event: self.new_input("*"))
        self.window.bind('%', lambda event: self.new_input("%"))
        self.window.bind('^', lambda event: self.new_input("^"))
        self.window.bind('(', lambda event: self.new_input("("))
        self.window.bind(')', lambda event: self.new_input(")"))
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
        self.window.bind('m', lambda event: self.ev_MRC()) 





    def __init__(self, num=0, memorylist=[], opnum=0):
        import tkinter as tk
        import calculator, utility
        self.tk = tk
        self.calculator = calculator
        self.utility = utility
        if num == 0:
            self.window = tk.Tk()
        self.is_seen = False
        self.memory_list = memorylist
        self.backward = 0
        self.opnum = opnum
        self.mm = 0


        self.binds()

        if num == 0:
            # frames
            frame1 = tk.Frame()
            frame1.pack(fill=tk.X)

            frame2 = tk.Frame()
            frame2.pack()

            # inputed label

            self.label = tk.Label(background="lightgray", height=3, master=frame1)
            self.label.pack(fill=tk.X)

            self.label2 = tk.Label(background="#4F6467", foreground="white", height=1, master=frame1)
            self.label2.pack(fill=tk.X)


            self.label3 = tk.Label(text="you had done nothing yet", background="lightgreen", foreground="black",
                                   master=frame2, wraplength=100)
            self.label3.grid(column=7, row=2, sticky="nswe")

            self.label4 = tk.Label(text=".........", background="lightgreen", foreground="black",
                                   master=frame2, wraplength=100)
            self.label4.grid(column=7, row=3, sticky="nswe")

            self.label5 = tk.Label(text=".........", background="lightgreen", foreground="black",
                                   master=frame2, wraplength=100)
            self.label5.grid(column=7, row=4, sticky="nswe")



            # buttons
            btn_0 = tk.Button(background="#FCA311", foreground="#14213D", text="0", height=5, width=10, master=frame2,
                              command=self.ev_0)
            btn_1 = tk.Button(background="#FCA311", foreground="#14213D", text="1", height=5, width=10, master=frame2,
                              command=self.ev_1)
            btn_2 = tk.Button(background="#FCA311", foreground="#14213D", text="2", height=5, width=10, master=frame2,
                              command=self.ev_2)
            btn_3 = tk.Button(background="#FCA311", foreground="#14213D", text="3", height=5, width=10, master=frame2,
                              command=self.ev_3)
            btn_4 = tk.Button(background="#FCA311", foreground="#14213D", text="4", height=5, width=10, master=frame2,
                              command=self.ev_4)
            btn_5 = tk.Button(background="#FCA311", foreground="#14213D", text="5", height=5, width=10, master=frame2,
                              command=self.ev_5)
            btn_6 = tk.Button(background="#FCA311", foreground="#14213D", text="6", height=5, width=10, master=frame2,
                              command=self.ev_6)
            btn_7 = tk.Button(background="#FCA311", foreground="#14213D", text="7", height=5, width=10, master=frame2,
                              command=self.ev_7)
            btn_8 = tk.Button(background="#FCA311", foreground="#14213D", text="8", height=5, width=10, master=frame2,
                              command=self.ev_8)
            btn_9 = tk.Button(background="#FCA311", foreground="#14213D", text="9", height=5, width=10, master=frame2,
                              command=self.ev_9)

            btn_plus = tk.Button(background="#FCA311", foreground="#14213D", text="+", height=5, width=10, master=frame2,
                                 command=self.ev_plus)
            btn_minus = tk.Button(background="#FCA311", foreground="#14213D", text="-", height=5, width=10, master=frame2,
                                  command=self.ev_minus)
            btn_multiple = tk.Button(background="#FCA311", foreground="#14213D", text="*", height=5, width=10,
                                     master=frame2, command=self.ev_multiple)
            btn_divide = tk.Button(background="#FCA311", foreground="#14213D", text="/", height=5, width=10, master=frame2,
                                   command=self.ev_divide)
            btn_equal = tk.Button(background="#FCA311", foreground="#14213D", text="=", height=5, width=10, master=frame2,
                                  command=self.ev_equal)
            btn_ashar = tk.Button(background="#FCA311", foreground="#14213D", text=".", height=5, width=10, master=frame2,
                                  command=self.ev_ashar)

            btn_parentheses_start = tk.Button(background="#FCA311", foreground="#14213D", text="(", height=5, width=10,
                                              master=frame2, command=self.ev_parentheses_start)
            btn_remaining = tk.Button(background="#FCA311", foreground="#14213D", text="%", height=5, width=10,
                                      master=frame2, command=self.ev_remaining)
            btn_last_answer = tk.Button(background="#FCA311", foreground="#14213D", text="Ans", height=5, width=10,
                                        master=frame2, command=self.ev_ans)
            btn_DEL = tk.Button(background="#FCA311", foreground="#14213D", text="DEL", height=5, width=20, master=frame2,
                                command=self.ev_DEL)
            btn_AC = tk.Button(background="#FCA311", foreground="#14213D", text="AC", height=5, width=20, master=frame2,
                               command=self.ev_AC)
            btn_parentheses_end = tk.Button(background="#FCA311", foreground="#14213D", text=")", height=5, width=10,
                                            master=frame2, command=self.ev_parentheses_end)
            btn_power = tk.Button(background="#FCA311", foreground="#14213D", text="^", height=5, width=10, master=frame2,
                                  command=self.ev_power)
            btn_memory = tk.Button(background="#FCA311", foreground="#14213D", text="mem", height=5, width=10,
                                   master=frame2, command=self.ev_mem)
            btn_change_mod = tk.Button(background="#FCA311", foreground="#14213D", text="mod", height=5, width=10,
                                       master=frame2, command=self.ev_change_mode)
            btn_sin = tk.Button(background="#FCA311", foreground="#14213D", text="sin", height=5, width=10,
                                master=frame2, command=self.ev_sin)
            btn_cos = tk.Button(background="#FCA311", foreground="#14213D", text="cos", height=5, width=10,
                                master=frame2, command=self.ev_cos)
            btn_tan = tk.Button(background="#FCA311", foreground="#14213D", text="tan", height=5, width=10,
                                master=frame2, command=self.ev_tan)
            btn_cot = tk.Button(background="#FCA311", foreground="#14213D", text="cot", height=5, width=10,
                                master=frame2, command=self.ev_cot)
            btn_log = tk.Button(background="#FCA311", foreground="#14213D", text="log", height=5, width=10,
                                master=frame2, command=self.ev_log)
            btn_ln = tk.Button(background="#FCA311", foreground="#14213D", text="ln", height=5, width=10,
                                master=frame2, command=self.ev_ln)
            btn_ft = tk.Button(background="#FCA311", foreground="#14213D", text="!!", height=5, width=10,
                                master=frame2, command=self.ev_ft)
            btn_00 = tk.Button(background="#FCA311", foreground="#14213D", text="00", height=5, width=10,
                                master=frame2, command=self.ev_00)
            btn_auto_r = tk.Button(background="#FCA311", foreground="#14213D", text="Auto\nreply", height=5, width=10,
                                master=frame2, command=self.ev_AR)
            btn_MRC = tk.Button(background="#FCA311", foreground="#14213D", text="MRC", height=5, width=10,
                                master=frame2, command=self.ev_MRC)
            btn_Mp = tk.Button(background="#FCA311", foreground="#14213D", text="M+", height=5, width=10,
                                master=frame2, command=self.ev_Mp)
            btn_Mm = tk.Button(background="#FCA311", foreground="#14213D", text="M-", height=5, width=10,
                                master=frame2, command=self.ev_Mm)


            btn_MRC.grid(column=0, row=1)

            btn_Mp.grid(column=0, row=2)



            btn_Mm.grid(column=0, row=3)

            btn_auto_r.grid(column=0, row=0)
            btn_00.grid(column=0, row=4)
            btn_sin.grid(column=6, row=1)
            btn_cos.grid(column=6, row=2)
            btn_tan.grid(column=6, row=3)
            btn_cot.grid(column=6, row=4)
            btn_ft.grid(column=4, row=0)
            btn_log.grid(column=6, row=0)
            btn_ln.grid(column=5, row=0)

            btn_power.grid(column=1, row=0)
            btn_memory.grid(column=2, row=0)
            btn_change_mod.grid(column=3, row=0)
            btn_DEL.grid(column=7, row=1)
            btn_AC.grid(column=7, row=0)
            btn_parentheses_end.grid(column=5, row=1)
            btn_parentheses_start.grid(column=4, row=1)
            btn_remaining.grid(column=4, row=4)
            btn_last_answer.grid(column=3, row=4)

            btn_7.grid(column=1, row=1)
            btn_8.grid(column=2, row=1)
            btn_9.grid(column=3, row=1)
            btn_4.grid(column=1, row=2)
            btn_5.grid(column=2, row=2)
            btn_6.grid(column=3, row=2)
            btn_1.grid(column=1, row=3)
            btn_2.grid(column=2, row=3)
            btn_3.grid(column=3, row=3)
            btn_0.grid(column=1, row=4)

            btn_ashar.grid(column=2, row=4)
            btn_equal.grid(column=5, row=4)
            btn_plus.grid(column=4, row=3)
            btn_minus.grid(column=5, row=3)
            btn_multiple.grid(column=4, row=2)
            btn_divide.grid(column=5, row=2)

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

    def binds(self):
        self.window.bind('0', lambda event: self.ev_0())
        self.window.bind('1', lambda event: self.ev_1())
        self.window.bind('2', lambda event: self.ev_2())
        self.window.bind('3', lambda event: self.ev_3())
        self.window.bind('4', lambda event: self.ev_4())
        self.window.bind('5', lambda event: self.ev_5())
        self.window.bind('6', lambda event: self.ev_6())
        self.window.bind('7', lambda event: self.ev_7())
        self.window.bind('8', lambda event: self.ev_8())
        self.window.bind('9', lambda event: self.ev_9())
        self.window.bind('.', lambda event: self.new_input("."))
        self.window.bind('+', lambda event: self.new_input("+"))
        self.window.bind('-', lambda event: self.new_input("-"))
        self.window.bind('/', lambda event: self.new_input("/"))
        self.window.bind('*', lambda event: self.new_input("*"))
        self.window.bind('%', lambda event: self.new_input("%"))
        self.window.bind('^', lambda event: self.new_input("^"))
        self.window.bind('(', lambda event: self.new_input("("))
        self.window.bind(')', lambda event: self.new_input(")"))

        self.window.bind('q', lambda event: quit())
        self.window.bind('e', lambda event: quit())
        self.window.bind('=', lambda event: self.ev_equal())
        self.window.bind('<Return>', lambda event: self.ev_equal())
        self.window.bind('<BackSpace>', lambda event: self.ev_DEL())
        self.window.bind('<Escape>', lambda event: self.ev_AC())
        self.window.bind('<Tab>', lambda event: self.ev_change_mode())
        self.window.bind('<space>', lambda event: self.ev_mem())
        self.window.bind('@', lambda event: self.ev_ans())


    def __init__(self, memorylist=[], opnum=0):
        import tkinter as tk
        import calculator, utility
        self.tk = tk
        self.calculator = calculator
        self.utility = utility
        self.window = tk.Tk()
        self.is_seen = False
        self.memory_list = memorylist
        self.backward = 0
        self.opnum = opnum
        self.binds()
        # frames
        frame1 = tk.Frame()
        frame1.pack(fill=tk.X)

        frame2 = tk.Frame()
        frame2.pack()

        # inputed label

        self.label = tk.Label(background="lightgray", height=3, master=frame1)
        self.label.pack(fill=tk.X)

        self.label2 = tk.Label(background="#4F6467", foreground="white", height=1, master=frame1)
        self.label2.pack(fill=tk.X)

        # buttons
        btn_0 = tk.Button(background="#FCA311", foreground="#14213D", text="0", height=5, width=10, master=frame2,
                          command=self.ev_0)
        btn_1 = tk.Button(background="#FCA311", foreground="#14213D", text="1", height=5, width=10, master=frame2,
                          command=self.ev_1)
        btn_2 = tk.Button(background="#FCA311", foreground="#14213D", text="2", height=5, width=10, master=frame2,
                          command=self.ev_2)
        btn_3 = tk.Button(background="#FCA311", foreground="#14213D", text="3", height=5, width=10, master=frame2,
                          command=self.ev_3)
        btn_4 = tk.Button(background="#FCA311", foreground="#14213D", text="4", height=5, width=10, master=frame2,
                          command=self.ev_4)
        btn_5 = tk.Button(background="#FCA311", foreground="#14213D", text="5", height=5, width=10, master=frame2,
                          command=self.ev_5)
        btn_6 = tk.Button(background="#FCA311", foreground="#14213D", text="6", height=5, width=10, master=frame2,
                          command=self.ev_6)
        btn_7 = tk.Button(background="#FCA311", foreground="#14213D", text="7", height=5, width=10, master=frame2,
                          command=self.ev_7)
        btn_8 = tk.Button(background="#FCA311", foreground="#14213D", text="8", height=5, width=10, master=frame2,
                          command=self.ev_8)
        btn_9 = tk.Button(background="#FCA311", foreground="#14213D", text="9", height=5, width=10, master=frame2,
                          command=self.ev_9)

        btn_plus = tk.Button(background="#FCA311", foreground="#14213D", text="+", height=5, width=10, master=frame2,
                             command=self.ev_plus)
        btn_minus = tk.Button(background="#FCA311", foreground="#14213D", text="-", height=5, width=10, master=frame2,
                              command=self.ev_minus)
        btn_multiple = tk.Button(background="#FCA311", foreground="#14213D", text="*", height=5, width=10,
                                 master=frame2, command=self.ev_multiple)
        btn_divide = tk.Button(background="#FCA311", foreground="#14213D", text="/", height=5, width=10, master=frame2,
                               command=self.ev_divide)
        btn_equal = tk.Button(background="#FCA311", foreground="#14213D", text="=", height=5, width=10, master=frame2,
                              command=self.ev_equal)
        btn_ashar = tk.Button(background="#FCA311", foreground="#14213D", text=".", height=5, width=10, master=frame2,
                              command=self.ev_ashar)

        btn_parentheses_start = tk.Button(background="#FCA311", foreground="#14213D", text="(", height=5, width=10,
                                          master=frame2, command=self.ev_parentheses_start)
        btn_remaining = tk.Button(background="#FCA311", foreground="#14213D", text="%", height=5, width=10,
                                  master=frame2, command=self.ev_remaining)
        btn_last_answer = tk.Button(background="#FCA311", foreground="#14213D", text="Ans", height=5, width=10,
                                    master=frame2, command=self.ev_ans)
        btn_DEL = tk.Button(background="#FCA311", foreground="#14213D", text="DEL", height=5, width=10, master=frame2,
                            command=self.ev_DEL)
        btn_AC = tk.Button(background="#FCA311", foreground="#14213D", text="AC", height=5, width=10, master=frame2,
                           command=self.ev_AC)
        btn_parentheses_end = tk.Button(background="#FCA311", foreground="#14213D", text=")", height=5, width=10,
                                        master=frame2, command=self.ev_parentheses_end)
        btn_power = tk.Button(background="#FCA311", foreground="#14213D", text="^", height=5, width=10, master=frame2,
                              command=self.ev_power)
        btn_memory = tk.Button(background="#FCA311", foreground="#14213D", text="mem", height=5, width=10,
                               master=frame2, command=self.ev_mem)
        btn_change_mod = tk.Button(background="#FCA311", foreground="#14213D", text="mod", height=5, width=10,
                                   master=frame2, command=self.ev_change_mode)

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

    def ev_power(self):
        self.new_input("^")

    def ev_remaining(self):
        self.new_input("%")

    def ev_parentheses_start(self):
        self.new_input("(")

    def ev_parentheses_end(self):
        self.new_input(")")

    def ev_change_mode(self):
        self.window.destroy()
        global advanced_interface
        b = advanced_interface(memorylist=self.memory_list, opnum=self.opnum)

    def ev_AC(self):
        self.label.config(text="")
        self.label2.config(text="")
        self.memory_list = []
        self.opnum = 0

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


a = simple_interface()


