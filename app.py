
from flask import Flask, render_template, request
import joblib
import os
import re

app = Flask(__name__)

MODEL_PATH = os.path.join("model", "spam_model.pkl")
model = joblib.load(MODEL_PATH)

SUSPICIOUS_TERMS = [
    "urgent", "winner", "won", "prize", "claim", "free",
    "cash", "reward", "lottery", "congratulations",
    "click here", "limited time", "offer", "http://",
    "https://", "verify account", "password", "bank"
]


def analyze_message(message):
    prediction = model.predict([message])[0]

    # This is the model's estimated probability for its predicted class,
    # not a guarantee that the prediction is correct.
    probabilities = model.predict_proba([message])[0]
    classes = list(model.classes_)
    confidence = float(probabilities[classes.index(prediction)]) * 100

    message_lower = message.lower()
    detected_terms = [
        term for term in SUSPICIOUS_TERMS
        if term in message_lower
    ]

    links = re.findall(r"https?://\S+", message, flags=re.IGNORECASE)

    return {
        "prediction": "SPAM" if prediction == "spam" else "NOT SPAM",
        "confidence": round(confidence, 2),
        "suspicious_terms": detected_terms,
        "links_found": len(links)
    }


@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    message = ""

    if request.method == "POST":
        message = request.form.get("message", "").strip()

        if not message:
            result = {"prediction": "Please enter a message."}
        elif len(message) > 5000:
            result = {"prediction": "Message must be 5000 characters or fewer."}
        else:
            result = analyze_message(message)

    return render_template(
        "index.html",
        result=result,
        message=message
    )


if __name__ == "__main__":
   app.run(host="0.0.0.0", port=5000, debug=False)
