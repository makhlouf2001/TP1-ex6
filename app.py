from flask import Flask
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient("mongodb://mongo:27017/")

db = client["testdb"]
collection = db["messages"]

@app.route("/")
def hello():
    if collection.count_documents({}) == 0:
        collection.insert_one({"message": "Hello from Flask & MongoDB!"})
    
    msg = collection.find_one()
    return msg["message"]

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
