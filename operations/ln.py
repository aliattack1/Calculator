def action(num1, num2):
    import math as m
    pre_answer = round(m.log(num2, m.e), 2)
    return num1 * pre_answer
