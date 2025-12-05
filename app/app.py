# Author:  Jayant Danech
# Date: 05.12.2025
# Timestamp application

from datetime import datetime, timezone
from flask import Flask, request, jsonify
import os

app = Flask(__name__)

def get_client_ip():
    # Check X-forwarded-for if seen
    xff = request.headers.get("X-Forwarded-for", "")
    if xff:
        return xff.split(",")[0].strip()

    # Fallback to remote address    
    return request.remote_addr or "not known"

@app.route("/", methods=["GET"])

def index():
    time_now = datetime.now(timezone.utc).astimezone().isoformat()
    client_ip = get_client_ip()
    return jsonify({
        "timestamp": time_now,
        "ip": client_ip
    })

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
