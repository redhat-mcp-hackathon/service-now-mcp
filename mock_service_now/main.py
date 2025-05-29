from fastapi import FastAPI, Path, Request
from fastapi.responses import JSONResponse

app = FastAPI()

@app.post("/api/sn_sc/v1/servicecatalog/items/{item_id}/submit_producer")
async def submit_producer(item_id: str = Path(...)):
    return {
        "result": {
            "status": "submitted",
            "item_id": item_id
        }
    }

@app.get("/help")
async def get_help(id: str, table: str, sys_id: str):
    return {
        "help_id": id,
        "table": table,
        "sys_id": sys_id,
        "message": "Mock help response"
    }
