from fastapi.testclient import TestClient
from main import app
import plazeholder as pz

client = TestClient(app)

def test_fizzbuzzList_OK():
    response = client.get("/fizzbuzzList/")
    assert response.status_code == 200
    assert len(response.json()) == 10

def test_fizzbuzzList_NotFound():
    response = client.get("/fizzbuzzList/1")
    assert response.status_code == 404
    assert response.json() ==  {"detail": "Not Found"}

def test_fizzbuzz_Fizz():
    response = client.get("/fizzbuzz/3")
    assert response.status_code == 200
    assert response.json()["fizzbuzz"] == "Fizz"

def test_fizzbuzz_Buzz():
    response = client.get("/fizzbuzz/5")
    assert response.status_code == 200
    assert response.json()["fizzbuzz"] == "Buzz"

def test_fizzbuzz_FizzBuzz():
    response = client.get("/fizzbuzz/15")
    assert response.status_code == 200
    assert response.json()["fizzbuzz"] == "FizzBuzz"

def test_fizzbuzz_Null():
    response = client.get("/fizzbuzz/1")
    assert response.status_code == 200
    assert response.json()["fizzbuzz"] == None

def test_fizzbuzz_ErrorParam():
    response = client.get("/fizzbuzz/jsrghsrc")
    assert response.status_code == 422
    assert response.json() == {
        "detail": [
            {
                "loc": [
                    "path",
                    "number"
                ],
                "msg": "value is not a valid integer",
                "type": "type_error.integer"
            }
        ]
    }