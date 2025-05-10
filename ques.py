from fastapi import FastAPI, Request
from pydantic import BaseModel
from typing import List, Union

app = FastAPI()

class input(BaseModel):
    data: List[str]

@app.post("/")
def process_data(payload: input):
    even = []
    odd = []
    alphabets = []

    for item in payload.data:
        if item.isdigit():
            num = int(item)
            if num % 2 == 0:
                even.append(item)
            else:
                odd.append(item)
        elif item.isalpha():
            alphabets.append(item.upper())

    return {
        "is_success": True,
        "user_id": "john_doe_17091999",
        "email": "john@xyz.com",
        "roll_number": "ABCD123",
        "odd_numbers": odd,
        "even_numbers": even,
        "alphabets": alphabets
    }
