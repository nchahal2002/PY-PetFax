# config
from flask import Flask # type: ignore
app = Flask(__name__)

# index route
@app.route('/')
def index():
    return 'Hello, this is PetFax!'