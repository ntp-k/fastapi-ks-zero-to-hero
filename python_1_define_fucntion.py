from customer_data import customer_data

def get_customer_data():
    return customer_data

# get data of customer
def get_customer_data_by_id(customer_id):
    if customer_id not in customer_data:
        return None
    
    return customer_data[customer_id]

def get_customer_email_by_id(customer_id):
    if customer_id not in customer_data:
        return None
    
    return customer_data[customer_id]['email']

def get_customer_phone_number_by_id(customer_id):
    if customer_id not in customer_data:
        return None
    
    return customer_data[customer_id]['phoneNo']

def update_customer_email_by_id(customer_id, new_email):
    if customer_id not in customer_data:
        return None

    customer_data[customer_id]['email'] = new_email
    return customer_data[customer_id]['email']

def add_new_customer(new_customer):
    customer_data[new_customer['customerId']] = new_customer
    return customer_data[new_customer['customerId']]

def delete_customer_by_id(customer_id):
    if customer_id not in customer_data:
        return None

    del customer_data[customer_id]



# EOF
