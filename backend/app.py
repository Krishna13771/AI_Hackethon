from flask import Flask, request
from lambda_handler import handler
from dotenv import load_dotenv
import json

load_dotenv()   # loads .env

app = Flask(__name__)

@app.route("/generate", methods=["POST"])
def generate():
    event = {"body": request.get_json()}
    response = handler(event, None)
    return (response["body"], response["statusCode"], response.get("headers", {}))

if __name__ == "__main__":
    print("Starting Flask backend...")
    app.run(host="127.0.0.1", port=5000, debug=True)
