from pymongo import MongoClient

MONGO_URI = "MONGO_URL"
client = MongoClient(MONGO_URI)

db = client["QR_Database"]
qr_collection = db["qrcodes"]