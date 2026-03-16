from enum import Enum
from random import randint

from pydantic import BaseModel, Field 


def random_destination(): 
    return randint(11000, 11999) 




class ShipmentStatus(str, Enum) :
    placed: str = "placed"
    in_transit: str  = "in_transit"
    out_for_delivery = "out_for_delivery"
    delivered = "delivered" 

#we use field to set restrictions 
class BaseShipment(BaseModel): 
    content: str = Field(description = " Contents of shipment" , max_length=30) 
    weight: float = Field(description = "Weight of shipment in kg", le = 25, ge = 1 ) #lt= less than, le= less than or equal, ge = greater than or equal to; used it to indiciate there has to be minimume weight of 1 
    destination: int | None = Field(description = "Destination zipcode", default_factory= random_destination) 


#having a base class, we can use inhertance which makes all new classes pydantic models 
class ShipmentRead(BaseShipment):
    status: ShipmentStatus


#making it a basemodel uses pydantic (enforces type/data validation during runtime )
class ShipmentCreate(BaseShipment): 
    pass

class ShipmentUpdate(BaseModel): 
    status: ShipmentStatus