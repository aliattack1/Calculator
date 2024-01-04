def action(inp):
    if inp.lower() =="exit" or inp.lower() =="quit":
        quit()
    start_p_count = 0
    end_p_count = 0
    for letter in inp:
        if letter == "(":
            start_p_count += 1
        elif letter == ")":
            end_p_count += 1
    if start_p_count == end_p_count:
        parentheses_finished = True
    else:
        parentheses_finished = False

    if not parentheses_finished:
        raise Exception("you have a wrong used parentheses fix it and retry")

    inp_without_space = ""
    for char in inp:
        if char != " ":
            inp_without_space += char

    inp = inp_without_space
    return inp
