import pytest

from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True

    with app.test_client() as client:
        yield client


def test_home_page(client):
    response = client.get("/")

    assert response.status_code == 200


def test_valid_feedback(client):
    response = client.post("/", data={
        "name": "Bhaskar Roy",
        "email": "bhaskar@niet.co.in",
        "erp": "123456",
        "course": "B.Tech Data Science",
        "feedback": "Very good course"
    })

    assert response.status_code == 200
    assert b"Feedback submitted successfully!" in response.data


def test_invalid_email(client):
    response = client.post("/", data={
        "name": "Bhaskar Roy",
        "email": "bhaskar@gmail.com",
        "erp": "123456",
        "course": "B.Tech Data Science",
        "feedback": "Very good course"
    })

    assert response.status_code == 200
    assert b"Please use your NIET email ID" in response.data


def test_missing_field(client):
    response = client.post("/", data={
        "name": "Bhaskar Roy",
        "email": "bhaskar@niet.co.in",
        "erp": "",
        "course": "B.Tech Data Science",
        "feedback": "Very good course"
    })

    assert response.status_code == 200
    assert b"All fields are required." in response.data
