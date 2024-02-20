from customer_data import customer_data
from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder

def get_customer_data():
    return customer_data

# get data of customer
def get_customer_data_by_id(customer_id):
    if customer_id not in customer_data:
        raise HTTPException(status_code=404, detail=f"customer not found ({customer_id})")
    
    return customer_data[customer_id]

def get_customer_email_by_id(customer_id):
    if customer_id not in customer_data:
        raise HTTPException(status_code=404, detail=f"customer not found ({customer_id})")

    return customer_data[customer_id]['email']

def get_customer_phone_number_by_id(customer_id):
    if customer_id not in customer_data:
        raise HTTPException(status_code=404, detail=f"customer not found ({customer_id})")
    
    return customer_data[customer_id]['phoneNo']

def update_customer_by_id(customer_id, update_customer_data):
    if customer_id not in customer_data:
        raise HTTPException(status_code=404, detail=f"customer not found ({customer_id})")

    updated_data = jsonable_encoder(update_customer_data)
    customer_data[customer_id] = updated_data
    return customer_data[customer_id]

def add_new_customer(new_customer):
    if new_customer.customerId in customer_data:
        raise HTTPException(status_code=404, detail=f"customer not found ({new_customer.customerId})")

    # data = {
    #     "customerId": new_customer.customerId,
    #     "customerName": new_customer.customerName,
    #     "email": new_customer.email,
    #     "phoneNo": new_customer.phoneNo
    # }
    data = jsonable_encoder(new_customer)
    customer_data[new_customer.customerId] = data
    return customer_data[new_customer.customerId]

def delete_customer_by_id(customer_id):
    if customer_id not in customer_data:
        raise HTTPException(status_code=404, detail=f"customer not found ({customer_id})")
    
    return_data = customer_data[customer_id]
    del customer_data[customer_id]
    return return_data



# EOF
