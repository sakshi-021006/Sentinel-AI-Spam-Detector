
import os
import joblib
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)

DATASET_PATH = "SMSSpamCollection"
MODEL_PATH = os.path.join("model", "spam_model.pkl")

# Load the real SMS Spam Collection dataset.
if not os.path.exists(DATASET_PATH):
    raise FileNotFoundError(
        "SMSSpamCollection was not found. "
        "Download and extract the UCI dataset, then place "
        "the file in your project folder."
    )

data = pd.read_csv(
    DATASET_PATH,
    sep="\t",
    header=None,
    names=["label", "message"],
    encoding="utf-8",
    on_bad_lines="skip"
)

data = data.dropna(subset=["label", "message"])
data["label"] = data["label"].str.strip().str.lower()
data = data[data["label"].isin(["ham", "spam"])]
data = data.drop_duplicates(subset=["label", "message"])

X = data["message"].astype(str)
y = data["label"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

model = Pipeline([
    ("tfidf", TfidfVectorizer(
        lowercase=True,
        strip_accents="unicode",
        ngram_range=(1, 2),
        sublinear_tf=True
    )),
    ("classifier", MultinomialNB(alpha=0.5))
])

print(f"Total messages: {len(data)}")
print(f"Training messages: {len(X_train)}")
print(f"Testing messages: {len(X_test)}")
print("\nTraining model...")

model.fit(X_train, y_train)

predictions = model.predict(X_test)

print("\nModel evaluation")
print("----------------")
print(f"Accuracy: {accuracy_score(y_test, predictions):.2%}")
print("\nClassification report:")
print(classification_report(
    y_test,
    predictions,
    labels=["ham", "spam"],
    target_names=["Not Spam", "Spam"],
    zero_division=0
))
print("Confusion matrix (rows = actual, columns = predicted):")
print(confusion_matrix(y_test, predictions, labels=["ham", "spam"]))

os.makedirs("model", exist_ok=True)
joblib.dump(model, MODEL_PATH)

print(f"\nModel saved successfully: {MODEL_PATH}")
