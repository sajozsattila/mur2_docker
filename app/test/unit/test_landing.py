from app.test.unit import client
import json

def test_landing(client):
    # test without header
    landing = client.get("/")
    jsondata = json.loads(landing.data.decode())
    assert {"name": 'Some flask skeleton', 'version': '1.0.0'} == jsondata
    assert landing.status_code == 200




