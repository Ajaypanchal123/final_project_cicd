from flask import Flask
import os
import json

app = Flask(__name__)

@app.route('/')
def index():
    return json.dumps({"message": "Hello from Flask Lambda!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
