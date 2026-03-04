
from typing import Any 

class City: 
    def __init__(self, name, location):
        self.name = name 
        self.location = location 





#we are specifiting that the digits is a list and the list contains only ints 
digits: list[int] = [1 ,2, 3, 4, 5]


#the table is a tuple. the tuple contains ints but the length is unknown 
table_5: tuple[int, ...] = ( 5, 10, 15, 20)  


#create a new instance of City 
Hamsphire = City("hampshire", 20453)
#we are hinting that the city temps must be a tuple. the tuple has a length of 2 where the first is a string and 2nd elemtn is temp in float    
city_temp: tuple[City, float] = (Hamsphire, 20.5)


#since we have key-value pairs, we are saying the key has to be a string, but the values can be either a string or an int 
shipment: dict[str, str | int ]  = { 
    "id" : 127 , 
    "weight" : 1.2, 
    "contnet" : "wooden table", 
    "status" : "in transit" 
}

#we can use Any instead which means our value can by any type 
shipment: dict[str, Any ]  = { 
    "id" : 127 , 
    "weight" : 1.2, 
    "contnet" : "wooden table", 
    "status" : "in transit" 
}

#this specifies that the input will be an int and the return type will be a float 
def root(num: int | float, exp : float | None  = .5 ) -> float: 
    if exp is None: 
        exp = .5
    return pow(num, .5) 


#specifiying this var can be either float or int 
number: int | float = 2 
optional: str | None 

optional = "value"

root_25  = root(15.5) 
