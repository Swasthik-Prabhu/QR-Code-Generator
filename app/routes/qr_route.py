import os
import qrcode
from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse
from bson import ObjectId
from models.qr_model import QRRequest
from database import qr_collection

from qrcode.constants import ERROR_CORRECT_H


router = APIRouter()


QR_DIR = "qrcodes"
os.makedirs(QR_DIR, exist_ok=True)

@router.post("/generate/")
async def generate_qr(data: QRRequest):
    """Generate a QR code and store it in MongoDB"""
    qr_id = str(ObjectId())  # Unique ID
    qr_path = os.path.join(QR_DIR, f"{qr_id}.png")

  
    qr = qrcode.QRCode(version=1, error_correction=qrcode.ERROR_CORRECT_H,
                       box_size=10, border=4)
    qr.add_data(data.link)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(qr_path)

    # Store in MongoDB
    qr_data = {"_id": qr_id, "link": data.link, "qr_code": qr_path}
    qr_collection.insert_one(qr_data)

    return {"qr_id": qr_id, "download_url": f"/download/{qr_id}"}

@router.get("/download/{qr_id}")
async def download_qr(qr_id: str):
    """Download the QR code by ID"""
    qr_data = qr_collection.find_one({"_id": qr_id})
    if not qr_data:
        raise HTTPException(status_code=404, detail="QR Code not found")
    
    return FileResponse(qr_data["qr_code"], media_type="image/png", filename=f"{qr_id}.png")