from flask import Flask

app=Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello,World!</>"

@app.route("/product")
def product():
    return "<p>Product</>"

@app.route("/product/egg")
def egg():
    return "<p>egg</>"