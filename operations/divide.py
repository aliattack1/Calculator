def action(num1, num2):
    if int(num2) != 0:
        return int(num1) / int(num2)
    else:
        raise "dont divide by zero"