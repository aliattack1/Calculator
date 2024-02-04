import operations as op
import utility


class Calculator:
    lnn = False
    operation_method_dict = {}
    operations_string = '@'
    negative_number = False
    negative_number_right = None
    operations_importance = ""
    importance_dictionary = {}
    function_list = []

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
        if last_number < 0:
            cls.lnn =True
            return -last_number
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
                    return cls.calculate(inp_part_2 + str(-int(new_inp)) + inp_part_3)
                else:
                    cls.negative_number = True
                    cls.negative_number_right = False
                    return cls.calculate(inp_part_2 + str(-new_inp) + inp_part_3)
        else:
            return cls.ordered_calculation_structure(inp)
    @classmethod
    def order_call(cls, inp, place):
        lis = utility.input_to_list.action(cls.function_list, cls.operations_string, inp)
        index = utility.get_index.action(lis, place-1)
        seperated_input_part = utility.get_string.action(lis[index-1:index+2])
        answer = cls.operations_and_functions(utility.input_to_list.action(cls.function_list, cls.operations_string, seperated_input_part))
        if cls.lnn:
            answer = -answer
            cls.lnn = False
        return utility.get_string.action(lis[:index - 1]) + str(answer) + utility.get_string.action(lis[index + 2:])

    @classmethod
    def ordered_calculation_structure(cls, inp):
        importance_list = utility.input_to_importance_dict.action(cls, inp)
        importance_list_keys = list(importance_list.keys())
        importance_list_values = []
        for key in importance_list_keys:
            importance_list_values.append(importance_list[key])
        if len(importance_list_values):
            while max(importance_list_values) > 1:
                max_importance_value = max(importance_list_values)
                importance_values_string = ""
                for key in importance_list_keys:
                    importance_values_string += str(importance_list[key])
                inp = cls.order_call(inp, importance_list_keys[importance_values_string.index(str(max_importance_value))])
                importance_list = utility.input_to_importance_dict.action(cls, inp)

                importance_list_keys = list(importance_list.keys())
                importance_list_values = []
                for key in importance_list_keys:
                    importance_list_values.append(importance_list[key])
                try:
                    return float(inp)
                except:
                    pass
        if utility.input_to_list.action(cls.function_list, cls.operations_string, inp)[0] == "-":
            return inp
        answer = cls.operations_and_functions(utility.input_to_list.action(cls.function_list, cls.operations_string, inp))
        if cls.lnn:
            answer = -answer
            cls.lnn = False
        return answer


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

if __name__ == "__main__":
    print(Calculator.calculate(utility.input_checker.action(input())))
