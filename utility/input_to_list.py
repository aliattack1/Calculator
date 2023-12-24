def action(function_list, operations_string, inp, retmod=0):
    output_list = []
    used_operation_list = []
    used_operation_index_list = []
    operation_list_loop_count = 0
    used_function_list = []
    used_function_index_list = []

    functions_finished = False
    while not functions_finished:
        found_function = False
        for i in function_list:
            if i in inp:
                used_function_list.append(i)
                inp = inp[:inp.find(i)] + "@" + inp[inp.find(i) + len(i):]
                found_function = True
        if not found_function:
            functions_finished = True

    for letter in inp:
        if letter in operations_string:
            if letter == "@":
                used_operation_list.append(used_function_list[0])
                used_function_list.pop(0)
                used_operation_index_list.append(operation_list_loop_count)
            else:
                used_operation_list.append(letter)
                used_operation_index_list.append(operation_list_loop_count)
        operation_list_loop_count += 1

    if retmod == 1:
        return used_operation_list, used_operation_index_list

    output_list.append(inp[0:used_operation_index_list[0]])
    list_filing_loop_count = 0
    for operation_index in used_operation_index_list:
        output_list.append(used_operation_list[list_filing_loop_count])

        if len(used_operation_index_list) > list_filing_loop_count + 1:
            output_list.append(inp[operation_index + 1:used_operation_index_list[list_filing_loop_count + 1]])
        else:
            output_list.append(inp[operation_index + 1:])
        list_filing_loop_count += 1
    if retmod == 0:
        return output_list


