class Calculator:

	@staticmethod
	def plus(a, b):
		return int(a) + int(b)

	operation_method_dict = {'+': plus}
	operations_string = '+'
	negetive_number = False
	negetive_number_right = None
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
			print(inp2 + str(new_inp) + inp3)
			if new_inp >= 0 :
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
			return cls.operations(cls.input_to_list(inp))

	@classmethod
	def operation_register(cls, opname, func):
		cls.operation_method_dict[opname] = func
		cls.operations_string += opname


def minus(num1, num2):
	return int(num1) - int(num2)


Calculator.operation_register('-', minus)

print('    ', Calculator.calculate(input('     ')))
