def string_to_dict():
     item = input('Enter item, split key and value by ":" ').split(':')
     if len(item) != 2 or notitem[0]or not item[1]:
        print('Enter correct data')  
        return string_to_dict()
     dict_from_string = {item[0]: item[1]}
print('Dictionary:',dict_from_string)# Function callstring_to_dict()
# Function call
string_to_dict()

   
        

