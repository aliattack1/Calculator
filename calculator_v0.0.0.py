
inp = input()

operations_string = '+'

def input_to_list(inp):
	lis = []
	used_operation_list = []
	used_operation_index_list =[]
	count = 0
	global operations_string
	for i in inp:
		if i in operations_string:
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


def callop(num1, operation, num2):
	if operation == '+':
		return int(num1) + int(num2)



def operations(lis):
	global operations_string
	opcount = 0
	for i in lis :
		
		if i in operations_string:
			new_number = lis[opcount+1]
			print(callop(last_number, i, new_number))
		else :
			last_number = i
		opcount += 1
operations(input_to_list(inp))
