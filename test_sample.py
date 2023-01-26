import requests

def test_index():
    x = requests.get("http://localhost:5000/")

    body = x.json()

    assert len(body["data"]) == 10
    

def test_hello_world():
    x = requests.get("http://localhost:5000/hello-world")
    
    body = x.json()

    assert body["data"] == "Hello World!"