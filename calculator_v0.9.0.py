import operations as op


class Calculator:

    operation_method_dict = {}
    operations_string = '@'
    negative_number = False
    negative_number_right = None
    operations_importance = ""
    importance_dictionary = {}
    function_list = []
    @classmethod
    def input_checker(cls, inp):
        parentheses_finished = None
        countains_letter = None
        letters_string = "qwertyuioplkjhgfdsazxcvbnm"
        for char in inp:
            if char in letters_string:
                countains_letter = True
                break
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
        if countains_letter:
            pass
            # raise Exception("you used a letter in input we dont support variables so you should re try without letter")
        inp_without_space = ""
        for char in inp:
            if char != " ":
                inp_without_space += char

        inp = inp_without_space
        return inp

    @classmethod
    def parentheses(cls, inp):
        start_p_count = 0
        end_p_count = 0
        letter_count = 0
        for letter in inp:
            if letter == "(":
                start_p_count += 1
            elif letter == ")":
                end_p_count += 1
            if start_p_count == end_p_count != 0:
                break
            letter_count += 1
        inp1 = inp[:letter_count+1]
        left_parentheses_index = inp1.find('(')
        right_parenthesess_index = len(inp1) - (inp1[::-1].find(')')) - 1
        return inp[left_parentheses_index + 1:right_parenthesess_index], inp[0:left_parentheses_index], inp[right_parenthesess_index + 1:]

    @classmethod
    def input_to_list(cls, inp, retmod=0):
        output_list = []
        used_operation_list = []
        used_operation_index_list = []
        operation_list_loop_count = 0
        used_function_list = []
        used_function_index_list = []

        functions_finished = False
        while not functions_finished:
            found_function = False
            for i in cls.function_list:
                if i in inp:
                    used_function_list.append(i)
                    inp = inp[:inp.find(i)] + "@" + inp[inp.find(i)+len(i):]
                    found_function = True
            if not found_function:
                functions_finished = True

        for letter in inp:
            if letter in cls.operations_string:
                if letter =="@":
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


    @classmethod
    def callfu(cls, num1, function, num2):
        if function in cls.function_list:
            if cls.negative_number:
                cls.negative_number = False
                if cls.negative_number_right:
                    return float(cls.operation_method_dict[function](float(num1), -float(num2)))
            else:
                return float(cls.operation_method_dict[function](float(num1), float(num2)))

    @classmethod
    def callop(cls, num1, operation, num2):
        if operation in cls.operations_string:
            if cls.negative_number:
                cls.negative_number = False
                if cls.negative_number_right:
                    return float(cls.operation_method_dict[operation](float(num1), -float(num2)))
                else:
                    return float(cls.operation_method_dict[operation](-float(num1), float(num2)))
            else:
                return float(cls.operation_method_dict[operation](float(num1), float(num2)))

    @classmethod
    def operations_and_functions(cls, input_list):
        operation_count = 0
        last_number = input_list[0]
        for input_part in input_list:

            if input_part in cls.operations_string:
                new_number = input_list[operation_count + 1]
                last_number = cls.callop(last_number, input_part, new_number)
            elif input_part in cls.function_list:
                new_number = input_list[operation_count + 1]
                last_number = cls.callfu(last_number, input_part, new_number)
            operation_count += 1
        return last_number

    @classmethod
    def calculate(cls, inp):
        if '(' in inp or ')' in inp:
            inp_part_1, inp_part_2, inp_part_3 = cls.parentheses(inp)
            new_inp = cls.calculate(inp_part_1)
            if float(new_inp) >= 0:
                return cls.calculate(inp_part_2 + str(new_inp) + inp_part_3)
            else:
                if inp_part_2 != "":
                    cls.negative_number = True
                    cls.negative_number_right = True
                    return cls.calculate(inp_part_2 + str(-new_inp) + inp_part_3)
                else:
                    cls.negative_number = True
                    cls.negative_number_right = False
                    return cls.calculate(inp_part_2 + str(-new_inp) + inp_part_3)
        else:
            return cls.ordered_calculation_structure(inp)

    @classmethod
    def input_to_importance_dict(cls, inp):
        importance_dict = {}
        used_operation_list, used_operation_index_list = cls.input_to_list(inp, 1)
        count = 0
        for i in used_operation_index_list:
            importance_dict[i] = cls.importance_dict[used_operation_list[count]]
            count += 1
        return importance_dict


    @classmethod
    def index_finder(cls, lis, place):
        count = -1
        index = 1
        for i in lis:
            count += len(i)
            if count == place:
                return index
            index += 1


    @staticmethod
    def get_string(input_list):
        string = ""
        for part in input_list:
            string += part
        return string

    @classmethod
    def order_call(cls, inp, place):
        lis = cls.input_to_list(inp)
        index = cls.index_finder(lis, place-1)
        seperated_input_part = cls.get_string(lis[index-1:index+2])
        answer = cls.operations_and_functions(cls.input_to_list(seperated_input_part))
        return cls.get_string(lis[:index - 1]) + str(answer) + cls.get_string(lis[index + 2:])



    @classmethod
    def ordered_calculation_structure(cls, inp):
        importance_list = cls.input_to_importance_dict(inp)
        importance_list_keys = list(importance_list.keys())
        importance_list_values = []
        for key in importance_list_keys:
            importance_list_values.append(importance_list[key])
        while max(importance_list_values) > 1:
            max_importance_value = max(importance_list_values)
            importance_values_string = ""
            for key in importance_list_keys:
                importance_values_string += str(importance_list[key])
            inp = cls.order_call(inp, importance_list_keys[importance_values_string.index(str(max_importance_value))])
            importance_list = cls.input_to_importance_dict(inp)

            importance_list_keys = list(importance_list.keys())
            importance_list_values = []
            for key in importance_list_keys:
                importance_list_values.append(importance_list[key])
            if not importance_list_values:
                return inp
        return cls.operations_and_functions(cls.input_to_list(inp))


    @classmethod
    def operation_and_function_register(cls, opname, func):
        if len(opname) == 1:
            cls.operation_method_dict[opname] = func
            cls.operations_string += opname
        else:
            cls.operation_method_dict[opname] = func
            cls.function_list.append(opname)


for key in op.dictionary:
    Calculator.operation_and_function_register(key, op.dictionary[key].action)
Calculator.importance_dict = op.importance_dictionary

print(Calculator.calculate(Calculator.input_checker(input())))

