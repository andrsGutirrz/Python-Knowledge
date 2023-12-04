from fastapi import FastAPI


app = FastAPI()
app.title = "My FastApi"
app.version = "0.0.1"


@app.get("/", tags=["Home"])
def message():
    return "Hello World"