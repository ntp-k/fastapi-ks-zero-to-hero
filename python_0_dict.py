from customer_data import customer_data
import json

# show all customer data
print('all customer data')
print(customer_data)

# show customer data in format
print('\nformatted customer data')
print(json.dumps(customer_data, indent=4))

# show data of customer aaa
print('\ndata of customer aaa')
print(json.dumps(customer_data['aaa'], indent=4))

# show email of customer aaa
print('\nemail of customer aaa')
print(customer_data['aaa']['email'])

# show phone number of customer aaa
print('\nphone number of customer aaa')
print(customer_data['aaa']['phoneNo'])

# update and show email of customer aaa
print('\nupdate and show email of customer aaa')
customer_data['aaa']['email'] = 'info@a.com'
print(customer_data['aaa']['email'])

# add new customer
print('\nadd new customer ccc')
new_customer = {
        "customerId": "ccc",
        "customerName": "Company C",
        "email": "contact@c.com",
        "phoneNo": "222222"
}
customer_data['ccc'] = new_customer

# delete customer bbb
print('\ndelete customer bbb')
del customer_data['bbb']
print(json.dumps(customer_data, indent=4))


# EOF
