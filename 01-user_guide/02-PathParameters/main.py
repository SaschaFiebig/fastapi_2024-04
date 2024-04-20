from enum import Enum
from fastapi import FastAPI

app = FastAPI()


# class for setting predefined path's 
class ModelName(str, Enum):
    gpt = "GPT"
    llama = "Llama"
    mistral = "Mistral"


# for multiple functions, the order matters '/users/me' needs to be first because 
# it is more specific than '/users/{item_id}'

# also, you can't redefine a function, because the first one will always run

@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}

@app.get("/items/{item_id}")        # http://127.0.0.1:8000/items/foo
#async def read_item(item_id):      # here the value of item_id can be of any type 
async def read_item(item_id: str):  # the value of item_id has to be a string 
    return {"item_id": item_id}

@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.gpt:  # checking for value
        return {"model_name": model_name, "message": "You choose GPT"}
    
    if model_name.value == "Llama":  # checking for value 
        return {"model_name": model_name, "message": "You choose Llama"}

    return {"model_name": model_name, "message": "You choose neither GPT nor Llama"}

# it is not a good idea to just pass a path (e.g. /some/path) into a variable 
# and use it in the pass operation decorator 
@app.get("/files/{file_path:path}")  # this will prevent double // 
async def read_file(file_path: str):
    return {"file_path": file_path}
