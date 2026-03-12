from fastapi import FastAPI, status, HTTPException 
from scalar_fastapi import get_scalar_api_reference
from typing import Any 

app = FastAPI() 



shipments = {
    12732: { 
        "weight" : .6,
        "content": "glass doll ",
        "shipment_status": "placed"
    },
    12733: {
        "weight": 1.2,
        "content": "wooden table",
        "shipment_status": "in transit"
    },
    12734: {
        "weight": 0.3,
        "content": "ceramic vase",
        "shipment_status": "delivered"
    },
    12735: {
        "weight": 2.1,
        "content": "desk lamp",
        "shipment_status": "shipped"
    },
    12736: {
        "weight": 0.8,
        "content": "book set",
        "shipment_status": "processing"
    },
    12737: {
        "weight": 1.5,
        "content": "office chair",
        "shipment_status": "placed"
    },
    12738: {
        "weight": 0.4,
        "content": "phone case",
        "shipment_status": "delivered"
    }
}


@app.get("/shipment/latest") 
def get_latest_shipment(): 
    id = max(shipments.keys()) 
    return shipments[id] 


#created our first api endpoint 
@app.get("/shipment")  #use a "?" to indicate we are using query parameters 
def get_shipment(id: int | None = None ) -> dict[str, Any ]: 
    if not id: 
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND, 
            detail = "Given ID does not exists"
        ) 
        return shipments[id] 


    if id not in shipments: 
        return {"detail": "Given Id does not exists!" }
    return shipments[id]




@app.get("/shipment/{field}")
def get_shipment_feild(field: str, id: int)-> dict[ str, Any]: 
    return { 
        field: shipments[id][field]
    }


