from fastapi import FastAPI, status, HTTPException
from scalar_fastapi import get_scalar_api_reference
from typing import Any
from enum import Enum 

from schema import Shipment, ShipmentCreate, ShipmentRead,  ShipmentUpdate




app = FastAPI()





shipments = {
    12732: {"weight": 1, "content": "glass doll ", "shipment_status": "placed"},
    12733: {"weight": 1.2, "content": "wooden table", "shipment_status": "in transit"},
    12734: {"weight": 0.3, "content": "ceramic vase", "shipment_status": "delivered"},
    12735: {"weight": 2.1, "content": "desk lamp", "shipment_status": "shipped"},
    12736: {"weight": 0.8, "content": "book set", "shipment_status": "processing"},
    12737: {"weight": 1.5, "content": "office chair", "shipment_status": "placed"},
    12738: {"weight": 0.4, "content": "phone case", "shipment_status": "delivered"},
}


@app.get("/shipment/latest")
def get_latest_shipment():
    id = max(shipments.keys())
    return shipments[id]


# created our first api endpoint
@app.get("/shipment", response_model = ShipmentRead )  # use a "?" to indicate we are using query parameters
def get_shipment(id: int | None = None) ->Shipment:
    if not id:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Given ID does not exists"
        )
    
    return shipments[id] 


    # if id not in shipments:
    #     return {"detail": "Given Id does not exists!"}
    # return shipments[id]


@app.post("/shipment")
def submit_shipment(shipment: ShipmentCreate) -> dict[str, Any]:
    # weight = req_body["weight"]
    new_id = max(shipments.keys()) + 1


    shipments[new_id] = {"content": shipment.content, "weight": shipment.weight, "shipment_status": "placed"}

    return {"id": new_id}


# put method is used to replace ALL FIELDS
@app.put("/shipment")
def shipment_update(
    id: int, content: str, weight: float, status: str
) -> dict[str, Any]:
    shipments[id] = {"content": content, "weight": weight, "shipment_status": status}
    return shipments[id]





@app.patch("/shipment", response_model = ShipmentRead)
def patch_shipment(
    id: int,
    body: ShipmentUpdate
):
    shipment = shipments[id] 
    shipment.update(body) 
    shipments[id] = shipment
    return shipments[id]

@app.delete("/shipment") 
def delete_shipment(id: int)-> dict[str, str]: 
    shipments.pop(id) 
    return {"detail" : f"shipment with id #{id} is deleted!"}



@app.get("/shipment/{field}")
def get_shipment_feild(field: str, id: int) -> Any:
    return shipments[id][field]


# we have defined a custom documentation using opanapi specification
@app.get("/scalar", include_in_schema=False)
def get_scalar_docs():
    return get_scalar_api_reference(
        openapi_url=app.openapi_url,
        title="Scalar API",
    )
