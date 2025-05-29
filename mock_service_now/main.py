from fastapi import FastAPI, Path, Request
from fastapi.responses import JSONResponse
import uuid
import random

app = FastAPI()

def generate_ticket_number():
    return "GWS" + "".join(random.choices("0123456789", k=7))

@app.post("/api/sn_sc/v1/servicecatalog/items/{item_id}/submit_producer")
async def submit_producer(item_id: str = Path(...)):
    return JSONResponse(content={
        "result": {
            "sys_id": uuid.uuid4().hex,
            "number": generate_ticket_number()
        }
    })

@app.get("/help")
async def get_help(id: str, table: str, sys_id: str):
    return {
        "help_id": id,
        "table": table,
        "sys_id": sys_id,
        "message": "Mock help response"
    }
