from fastapi import FastAPI
from math_functions import add
import random

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello Gorrila", "value": str(add(random.randint(0, 12), random.randint(11, 30)))}