from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def first_api():
    return{"message":"Hello"}