from fastapi import FastAPI 
from scalar_fastapi import get_scalar_api_reference

app = FastAPI() 

#created our first api endpoint 
@app.get("/shipment")  #we can also have nested directories. ie. /seller/shipment 
def get_shipment(): 
    return { 
        "content": "wooden table",
        "shipment_status": "in transit"
    }


#we have defined a custom documentation using opanapi specification 
@app.get("/scalar", include_in_schema = False) 
def get_scalar_docs(): 
    return get_scalar_api_reference(
        openapi_url = app.openapi_url, 
        title = "Scalar API" , 
    )
