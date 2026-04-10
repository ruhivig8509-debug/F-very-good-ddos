from flask import Flask
import threading
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Server is Up and Running!</h1>"

def run_web():
    # Render automatically sets the PORT environment variable
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)

# Isko call karne se web service background mein chalne lagegi
def start_fake_service():
    threading.Thread(target=run_web, daemon=True).start()
