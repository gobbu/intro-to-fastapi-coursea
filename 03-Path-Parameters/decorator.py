
def custom_fence(fence: str = "+"): 



    def add_fence(func):
        
        def wrapper(text: str):
            print(fence * len(text) )
            func(text) 
            print(fence * len(text) )
        return wrapper
    #need to return the function 
    return add_fence

@custom_fence("&")
def log(text: str):
    print(text) 

log("balloon") 