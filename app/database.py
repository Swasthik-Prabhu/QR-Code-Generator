from pymongo import MongoClient

MONGO_URI = "mongodb+srv://swasthikp03:swasthik@swasthikprabhu.fabhbaq.mongodb.net/"
client = MongoClient(MONGO_URI)

db = client["QR_Database"]
qr_collection = db["qrcodes"]