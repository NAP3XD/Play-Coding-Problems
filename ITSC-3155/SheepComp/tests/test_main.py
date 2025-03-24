from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

def test_read_sheep():
    response = client.get("/sheep/1")
    
    # assert that the response status code is 200 
    assert response.status_code == 200
    # assert that the response JSON matches expected data
    assert response.json() == {
        "id": 1,
        "name": "Spice",
        "breed": "Gotland",
        "sex": "ewe"
    }

    # test function for adding new sheep
def test_add_sheep():

    # new sheep data
    test_sheep = {
        "id": 3,
        "name": "Moses",
        "breed": "Dog",
        "sex": "Male"
    }

# POST request with sheep data
    response = client.post("/sheep", json=test_sheep)

    assert response.status_code == 201

    # make sure response data matches
    response_data = response.json()
    for key in test_sheep:
        assert response_data[key] == test_sheep[key]

    # verify the sheep can be retreived
    sheep_id = response_data["id"]
    get_response = client.get(f"/sheep/{sheep_id}")
    assert get_response.status_code == 200

    # verify json data can be retrieved
    retrieve_data = get_response.json()
    for key in test_sheep:
        assert retrieve_data[key] == test_sheep[key]
