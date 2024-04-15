from fastapi import fastapi

app = FastAPI()


@app.get("/")
asznc def root():
    return {"message": "Hello FastAPI"}
