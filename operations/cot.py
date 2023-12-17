def action(num1, num2):
    import math as m
    pre_answer = round(m.tan(num2/180*m.pi), 2)**-1
    if num2 == 90:
        pre_answer = 0
    return num1 * pre_answer
