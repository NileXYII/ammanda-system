from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Vercel!"

# Expose the Flask app
from vercel_wsgi import make_lambda_handler
handler = make_lambda_handler(app)
