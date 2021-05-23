from typing import Optional
from fastapi import FastAPI, Response, status

app = FastAPI()
app.opStatus = 1

@app.get("/", status_code=200)
def read_root(response: Response):
    if app.opStatus == 1:
        return {"Hello": app.opStatus}
    else:
        response.status_code = status.HTTP_503_SERVICE_UNAVAILABLE
    
@app.get("/items/{item_id}")
def read_item(item_id: int, response: Response, q: Optional[str] = None):
    if app.opStatus == 1:
        return {"item_id": item_id, "q": q}
    else:
        response.status_code = status.HTTP_503_SERVICE_UNAVAILABLE

@app.get("/status/{item_id}", status_code=200)
def read_item(item_id: int, response: Response):
    if item_id == 503:
        app.opStatus = 0
        response.status_code = status.HTTP_503_SERVICE_UNAVAILABLE
    elif item_id == 200:
        app.opStatus = 1
        response.status_code = status.HTTP_200_OK
        return {"item_id": "Back to normal :)"}
    else:
        return {"item_id": "Returning the status"}
