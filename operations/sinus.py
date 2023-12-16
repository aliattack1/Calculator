def action(num1, num2):
    import math as m
    pre_answer = round(m.sin(num2/180*m.pi), 2)
    return num1 * pre_answer
