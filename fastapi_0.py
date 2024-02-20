from fastapi import FastAPI, File, UploadFile
from pydantic import BaseModel

import fastapi_1_service as my_service
import fastapi_2_file_service as file_service

app = FastAPI()


class Customer(BaseModel):
    customerId: str
    customerName: str
    email: str
    phoneNo: str


#----------------------------------------------------------#
#    Get                                                   #
#----------------------------------------------------------#
@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/customers")
def get_customer_data():
    return my_service.get_customer_data()

# @app.get("/customers")
# def get_customer_data(limit: int=0):
#     customer_data = my_service.get_customer_data()
#     if len(customer_data) < limit:
#         return customer_data
#     else:
#         return customer_data[:limit]

@app.get("/customer/{customerId}")
def get_customer_data_by_id(customerId: str):
    return my_service.get_customer_data_by_id(customer_id= customerId)

@app.get("/customer/{customerId}/email")
def get_customer_email_by_id(customerId: str):
    return my_service.get_customer_email_by_id(customer_id= customerId)

@app.get("/customer/{customerId}/phoneno")
def get_customer_phone_number_by_id(customerId: str):
    return my_service.get_customer_phone_number_by_id(customer_id= customerId)


#----------------------------------------------------------#
#    Put                                                   #
#----------------------------------------------------------#
@app.put("/customer/{customerId}")
def update_customer_by_id(customerId: str, customerData: Customer):
    return my_service.update_customer_by_id(customer_id= customerId, update_customer_data=customerData)

#----------------------------------------------------------#
#    Post                                                  #
#----------------------------------------------------------#
@app.post("/customer")
def create_customer(customer: Customer):
    return my_service.add_new_customer(new_customer=customer)


#----------------------------------------------------------#
#    Delete                                                #
#----------------------------------------------------------#
@app.delete("/customer/{customerId}")
def delete_customer(customerId: str):
    return my_service.delete_customer_by_id(customer_id=customerId)


#----------------------------------------------------------#
#    File                                                  #
#----------------------------------------------------------#
@app.post("/uploadfile/", tags=["file"])
async def create_upload_file(file: UploadFile):
    return file_service.read_file(file)

    # return {"filename": file.filename}

@app.post("/summarize-sale/", tags=["file"])
async def summarize_sale(file: UploadFile):
    return file_service.summarize_sale(file)

@app.post("/summarize-sale/csv", tags=["file"])
async def summarize_sale(file: UploadFile):
    return file_service.summarize_sale_to_csv(file)

# EOF
