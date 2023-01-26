from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    x = []
    for i in range(10):
        x.append((i+1)*100)
    
    return {"data": x}, 200


@app.route("/hello-world")
def hello_world():
    return {"data": "Hello World!"}, 200

if __name__ == "__main__":
    app.run()