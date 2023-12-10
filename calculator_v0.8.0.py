import operations as op


class Calculator:

    operation_method_dict = {}
    operations_string = ''
    negative_number = False
    negative_number_right = None
    operations_importance = ""
    importance_dictionary = {}

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
        print(inp1)
        left_parentheses_index = inp1.find('(')
        right_parenthesess_index = len(inp1) - (inp1[::-1].find(')')) - 1
        return inp[left_parentheses_index + 1:right_parenthesess_index], inp[0:left_parentheses_index], inp[right_parenthesess_index + 1:]

    @classmethod
    def input_to_list(cls, inp):
        output_list = []
        used_operation_list = []
        used_operation_index_list = []
        operation_list_loop_count = 0

        for letter in inp:
            if letter in cls.operations_string:
                used_operation_list.append(letter)
                used_operation_index_list.append(operation_list_loop_count)

            operation_list_loop_count += 1
        output_list.append(inp[0:used_operation_index_list[0]])
        list_filing_loop_count = 0
        for operation_index in used_operation_index_list:
            output_list.append(inp[operation_index])
            if len(used_operation_index_list) > list_filing_loop_count + 1:
                output_list.append(inp[operation_index + 1:used_operation_index_list[list_filing_loop_count + 1]])
            else:
                output_list.append(inp[operation_index + 1:])
            list_filing_loop_count += 1
        return output_list

    @classmethod
    def callop(cls, num1, operation, num2):
        if operation in cls.operations_string:
            if cls.negative_number:
                cls.negative_number = False
                if cls.negative_number_right:
                    return cls.operation_method_dict[operation](int(num1), -int(num2))
                else:
                    return cls.operation_method_dict[operation](-int(num1), int(num2))
            else:
                return cls.operation_method_dict[operation](int(num1), int(num2))

    @classmethod
    def operations(cls, input_list):
        operation_count = 0
        last_number = input_list[0]
        for input_part in input_list:

            if input_part in cls.operations_string:
                new_number = input_list[operation_count + 1]
                last_number = (cls.callop(last_number, input_part, new_number))
            operation_count += 1
        return last_number

    @classmethod
    def calculate(cls, inp):
        if '(' in inp or ')' in inp:
            inp_part_1, inp_part_2, inp_part_3 = cls.parentheses(inp)
            new_inp = cls.calculate(inp_part_1)
            if int(new_inp) >= 0:
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
        count = 0
        for i in inp:
            if i in cls.operations_string:
                importance_dict[count] = (op.importance_dictionary[i])
            count += 1
        return importance_dict


    @classmethod
    def index_finder(cls, lis, place):
        count = -1
        index = 0
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
        index = cls.index_finder(lis, place)
        seperated_input_part = cls.get_string(lis[index-1:index+2])
        answer = cls.operations(cls.input_to_list(seperated_input_part))
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
        return cls.operations(cls.input_to_list(inp))


    @classmethod
    def operation_register(cls, opname, func):
        cls.operation_method_dict[opname] = func
        cls.operations_string += opname


for key in op.dictionary:
    Calculator.operation_register(key, op.dictionary[key].action)
Calculator.importance_dict = op.importance_dictionary

print(Calculator.calculate(input()))

