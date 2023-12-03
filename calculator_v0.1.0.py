class calculator:
	
	
	
	operations_string = '+'
	
	@classmethod
	def input_to_list(cls, inp):
		lis = []
		used_operation_list = []
		used_operation_index_list =[]
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
		    	lis.append(inp[s:used_operation_index_list[new_count+1]])
		    else:
		    	lis.append(inp[s+1:])
		    new_count += 1
		return lis
	
	@staticmethod
	def callop(num1, operation, num2):
		if operation == '+':
			return int(num1) + int(num2)
	
	
	@classmethod
	def operations(cls, lis):
		opcount = 0
		for i in lis :
			
			if i in cls.operations_string:
				new_number = lis[opcount+1]
				print(cls.callop(last_number, i, new_number))
			else :
				last_number = i
			opcount += 1
	@classmethod
	def calculate(cls, inp):
		cls.operations(cls.input_to_list(inp))
	

calculator.calculate(input())
	