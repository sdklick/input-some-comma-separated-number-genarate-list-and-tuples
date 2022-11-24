# input some comma separated number genarate list and tuples

userinput = input('enter some number : ')

my_list = userinput.split(',')

my_tuple = tuple(my_list)

print('Your list : ', my_list)
print('Your Tuple : ', my_tuple)
