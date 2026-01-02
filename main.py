from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {
        "message": "SmallCloud API",
        "status": "running",
        "version": "0.1.0"
    }