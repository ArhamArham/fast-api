from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def index():
    return {"data": "hello from index"}


@app.get("/blog/{id}")
def show(id):
    return {"data": id}


@app.get("/blog/{id}/comments")
def comments(id):
    return {"id": id,'data':{'commets data;'}}
