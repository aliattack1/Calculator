import operations as op


class Calculator:

    operation_method_dict = {}
    operations_string = ''
    negetive_number = False
    negetive_number_right = None
    operations_importance = ""
    importance_dictionary = {}

    @classmethod
    def parantese(cls, inp):
        a = inp.find('(')
        b = inp[::-1].find(')')
        b = len(inp) - b - 1
        return inp[a + 1:b], inp[0:a], inp[b + 1:]

    @classmethod
    def input_to_list(cls, inp):
        lis = []
        used_operation_list = []
        used_operation_index_list = []
        count = 0

        for i in inp:
            if i in cls.operations_string:
                used_operation_list.append(i)
                used_operation_index_list.append(count)

            count += 1
        lis.append(inp[0:used_operation_index_list[0]])
        new_count = 0
        for s in used_operation_index_list:
            lis.append(inp[s])
            if len(used_operation_index_list) > new_count + 1:
                lis.append(inp[s + 1:used_operation_index_list[new_count + 1]])
            else:
                lis.append(inp[s + 1:])
            new_count += 1
        return lis

    @classmethod
    def callop(cls, num1, operation, num2):
        if operation in cls.operations_string:
            if cls.negetive_number:
                cls.negetive_number = False
                if cls.negetive_number_right:
                    return cls.operation_method_dict[operation](int(num1), -int(num2))
                else:
                    return cls.operation_method_dict[operation](-int(num1), int(num2))
            else:
                return cls.operation_method_dict[operation](int(num1), int(num2))

    @classmethod
    def operations(cls, lis):
        opcount = 0
        last_number = lis[0]
        for i in lis:

            if i in cls.operations_string:
                new_number = lis[opcount + 1]
                last_number = (cls.callop(last_number, i, new_number))
            opcount += 1
        return last_number

    @classmethod
    def calculate(cls, inp):
        if '(' in inp or ')' in inp:
            inp1, inp2, inp3 = cls.parantese(inp)
            new_inp = cls.calculate(inp1)
            if new_inp >= 0:
                return cls.calculate(inp2 + str(new_inp) + inp3)
            else:
                if inp2 != "":
                    cls.negetive_number = True
                    cls.negetive_number_right = True
                    return cls.calculate(inp2 + str(-new_inp) + inp3)
                else:
                    cls.negetive_number = True
                    cls.negetive_number_right = False
                    return cls.calculate(inp2 + str(-new_inp) + inp3)
        else:
            return cls.order(inp)

    @classmethod
    def importance_list(cls, inp):
        ilist = {}
        n = 0
        for i in inp:
            if i in cls.operations_string:
                ilist[n] = (op.importance_dictionary[i])
            n += 1
        return ilist


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
    def gstr(lis):
        l = ""
        for a in lis:
            l += a
        return l

    @classmethod
    def order_call(cls, inp, place):
        lis = cls.input_to_list(inp)
        index = cls.index_finder(lis, place)
        m = lis[index-1:index+2]
        l = cls.gstr(m)
        answer = cls.operations(cls.input_to_list(l))
        return cls.gstr(lis[:index-1]) + str(answer) + cls.gstr(lis[index+2:])



    @classmethod
    def order(cls, inp):
        imlist = cls.importance_list(inp)
        ilist = list(imlist.keys())
        nlist = []
        for i in ilist:
            nlist.append(imlist[i])

        while max(nlist) > 1:
            s = max(nlist)
            f = ""
            for a in ilist:
                f += str(imlist[a])
            inp = cls.order_call(inp, ilist[f.index(str(s))])
            imlist = cls.importance_list(inp)

            ilist = list(imlist.keys())
            nlist = []
            for i in ilist:
                nlist.append(imlist[i])
            if nlist == []:
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

