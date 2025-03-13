from fastapi import FastAPI
from routes.qr_route import router as qr_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="FastAPI QR Code Generator")

# Include Routes
app.include_router(qr_router, tags=["QR Code"])

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  
)


@app.get("/")
def home():
    return {"message": "Welcome to FastAPI QR Code Generator!"}
