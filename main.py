ask = input("\nt for text based interface and v for visual based interface:  ")
if ask.lower() == "t":
    import calculator
    while True:
        print(calculator.Calculator.calculate(calculator.utility.input_checker.action(input("enter a problem:   "))))
elif ask.lower() == "v":
    import interface