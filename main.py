from flask import Flask
import os 

hello_something = os.environ.get('HELLO_SOMETHING')
app = Flask(__name__)

@app.route('/')
def index():
    return f"Hello from {hello_something}"

app.run(host='0.0.0.0', port=81)