phonebook =[{ 'name':  'Andrew' ,  'mobile_phone' :9477865 , 'office_phone' :6612345 , 'email' : 'andrew@sutd.edu.sg'} ,
{ 'name': 'Bobby' , 'mobile_phone' :8123498 , 'office_phone' :6654321 , 'email': 'bobby@sutd.edu.sg '}]


def getDetails(input_name, input_key, phonebook):
	for i in phonebook:
		if i['name']== input_name:
			return i[input_key]
	
'''getDetails('Bobby','mobile_phone', phonebook)
getDetails('Bobby','office_phone', phonebook)
getDetails('Bobby','email', phonebook)
'''
print getDetails('Andrew', 'email', phonebook)