from app import app


def test_home_page():
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200


def test_feedback_submission():
    client = app.test_client()

    response = client.post(
        "/",
        data={
            "name": "Bhaskar",
            "course": "Data Science",
            "feedback": "The course was very helpful."
        }
    )

    assert response.status_code == 200
    assert b"Bhaskar" in response.data
