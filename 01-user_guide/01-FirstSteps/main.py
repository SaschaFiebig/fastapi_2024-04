from fastapi import FastAPI

# create fastapi instance 
app = FastAPI()  # uvicorn main:app --reload (to start application)
# my_awesome_api = FastAPI()  # uvicorn main:my_awesome_api --reload

# CRUD functionalitity
#@app.get()     Create
#@app.post()    Read
#@app.put()     Update
#@app.delete()  Delete

# path operation decorator e.g. http://127.0.0.1:8000/mz/data/
@app.get("/my/data/")
async def root():  # path operation function
    return {"message": "Hello FastAPI"}  # it is possible to return dict, list, str, int, ect. 
