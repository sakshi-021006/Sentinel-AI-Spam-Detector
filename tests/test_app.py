
import app as spam_app


def test_homepage_loads():
    client = spam_app.app.test_client()

    response = client.get("/")

    assert response.status_code == 200
    assert b"Sentinel" in response.data


def test_spam_message_analysis():
    result = spam_app.analyze_message(
        "Congratulations! You won a free prize. Click here now!"
    )

    assert result["prediction"] in ["SPAM", "NOT SPAM"]
    assert 0 <= result["confidence"] <= 100
    assert isinstance(result["suspicious_terms"], list)
    assert isinstance(result["links_found"], int)


def test_empty_message():
    client = spam_app.app.test_client()

    response = client.post("/", data={"message": ""})

    assert response.status_code == 200
    assert b"Please enter a message." in response.data


def test_message_too_long():
    client = spam_app.app.test_client()

    response = client.post("/", data={"message": "a" * 5001})

    assert response.status_code == 200
    assert b"5000 characters or fewer" in response.data
