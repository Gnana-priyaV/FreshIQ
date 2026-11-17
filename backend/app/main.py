from fastapi import FastAPI

app = FastAPI(title="FreshIQ")

@app.get("/")
def home():
    return {"message": "Welcome to FreshIQ!"}

@app.get("/fruits")
def list_fruits():
    return [
        {"id":1, "name": "Apple", "Price_Per_kg": 60},
        {"id":2, "name": "Banana", "Price_Per_kg": 40},
        {"id":3, "name": "Orange", "Price_Per_kg": 50}
    ]