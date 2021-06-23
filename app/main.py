from fastapi import FastAPI
from typing import Optional
import uvicorn
import fizzbuzz as fb
import plazeholder as pz

app = FastAPI(
    title="FizzBuzz Project",
    description="Project to calculate fizzbuzz of number and get plaze_holder information",
    version="1.0.0",
)

#This Endpoint get 10 first fizzbuzz entities
@app.get("/fizzbuzzList")
async def fizzbuzzList():
    result = []
    for i in range(1,11):
        fizzbuzzValue = fb.fizzbuzz(i)
        title,body = pz.plazeHolder(i)
        data = {"number": i, "fizzbuzz": fizzbuzzValue , "placeholder_post": {
                    "title": title,
                    "body": body
                    }
                }
        result.append(data)
    return result

#This Endpoint get fizzbuzz entitie of number param
@app.get("/fizzbuzz/{number}")
async def fizzbuzz(number: int):
    fizzbuzzValue = fb.fizzbuzz(number)
    title,body = pz.plazeHolder(number)
    data = {"number": number, "fizzbuzz": fizzbuzzValue , "placeholder_post": {
                    "title": title,
                    "body": body
                    }
                }
    return data

if __name__ == '__main__':
    uvicorn.run(app)
