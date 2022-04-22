from flask import Flask

app = Flask(__name__)

@app.route('/') # //www.google.com
def home():
    return "Hello World"

app.run(port=5000)
