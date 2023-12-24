from . import input_to_list


def action(cls, inp):
    importance_dict = {}
    used_operation_list, used_operation_index_list = input_to_list.action(cls.function_list, cls.operations_string, inp, 1)
    count = 0
    for i in used_operation_index_list:
        importance_dict[i] = cls.importance_dict[used_operation_list[count]]
        count += 1
    return importance_dict
