from fastapi import FastAPI

app = FastAPI()

app.add_middleware(
     CORSMiddleware,
     allow_origins=["*"],
     allow_credentials=True,
     allow_methods=["*"],
     allow_headers=["*"],
)
@app.get("/")
def homeScreen():
    return {"message": "hi"}
