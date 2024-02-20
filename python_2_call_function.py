import python_1_define_fucntion as my_func
import json

# show all customer data
print('all customer data')
customer_data = my_func.get_customer_data()
print(customer_data)

# show customer data in format
print('\nformatted customer data')
customer_data = my_func.get_customer_data()
print(json.dumps(customer_data, indent=4))

# show data of customer aaa
print('\ndata of customer aaa')
customer_a = my_func.get_customer_data_by_id(customer_id= 'aaa')
print(json.dumps(customer_a, indent=4))

# show email of customer aaa
print('\nemail of customer aaa')
customer_a_email = my_func.get_customer_email_by_id(customer_id= 'aaa')
print(customer_a_email)

# show phone number of customer aaa
print('\nphone number of customer aaa')
customer_a_phone = my_func.get_customer_phone_number_by_id(customer_id= 'aaa')
print(customer_a_phone)

# update and show email of customer aaa
print('\nupdate and show email of customer aaa')
customer_a_email = my_func.update_customer_email_by_id(customer_id='aaa', new_email='info@a.com')
print(customer_a_email)

# add new customer
print('\nadd new customer ccc')
new_customer = {
        "customerId": "ccc",
        "customerName": "Company C",
        "email": "contact@c.com",
        "phoneNo": "222222"
}
my_func.add_new_customer(new_customer=new_customer)
customer_data = my_func.get_customer_data()
print(json.dumps(customer_data, indent=4))

# delete customer bbb
print('\ndelete customer bbb')
my_func.delete_customer_by_id(customer_id='bbb')

# show customer data
customer_data = my_func.get_customer_data()
print(json.dumps(customer_data, indent=4))

# EOF
