from fastapi import FastAPI

app = FastAPI(title="Price Intelligence API")

@app.get("/health")
def health():
    return {"status": "ok"}