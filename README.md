# Sentinel AI – AI Spam Message Detector

## Overview
Sentinel AI is a Machine Learning-based web application that detects whether an SMS message is **Spam** or **Not Spam**. It uses Natural Language Processing (NLP) techniques to analyze message text and classify messages through a trained Machine Learning model.

The project provides a simple web interface built with Flask and supports Docker containerization and automated testing using Jenkins.

## Features
- SMS spam and legitimate message classification
- Text preprocessing and feature extraction using TF-IDF
- Machine Learning classification using Multinomial Naive Bayes
- Interactive web dashboard using Flask, HTML, and CSS
- Trained model saved for reuse
- Automated application tests using pytest
- Docker image and container support
- Jenkins pipeline for automated testing and build status reporting

## Technologies Used
- **Programming Language:** Python
- **Machine Learning:** Scikit-learn
- **NLP / Feature Extraction:** TF-IDF
- **Algorithm:** Multinomial Naive Bayes
- **Web Framework:** Flask
- **Frontend:** HTML, CSS
- **Testing:** pytest
- **Containerization:** Docker
- **CI:** Jenkins
- **Source Code Management:** Git and GitHub

## Project Structure

```text
AI-Spam-Detector/
├── app.py
├── train_model.py
├── requirements.txt
├── Dockerfile
├── .dockerignore
├── .gitignore
├── SMSSpamCollection
├── model/
│   └── spam_model.pkl
├── templates/
│   └── index.html
├── static/
│   └── style.css
└── tests/
    └── test_app.py
```

## How It Works
1. The user enters an SMS message in the web application.
2. The text is transformed into numerical features using the trained TF-IDF vectorizer.
3. The Multinomial Naive Bayes model analyzes the features.
4. The application displays the predicted classification: Spam or Not Spam.

## Installation and Setup

### Prerequisites
- Python 3
- pip
- Docker Desktop (for containerized execution)

### Run Locally

1. Clone the repository:

   ```bash
   git clone https://github.com/sakshi-021006/Sentinel-AI-Spam-Detector.git
   ```

2. Open the project directory:

   ```bash
   cd Sentinel-AI-Spam-Detector
   ```

3. Create and activate a virtual environment on Windows:

   ```powershell
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   ```

4. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. Start the application:

   ```bash
   python app.py
   ```

6. Open the application in your browser:

   ```text
   http://localhost:5000
   ```

## Docker Setup

Build the Docker image:

```bash
docker build -t sentinel-ai-spam-detector .
```

Run the container:

```bash
docker run --name sentinel-ai -p 5000:5000 sentinel-ai-spam-detector
```

Open `http://localhost:5000` in your browser.

To stop the running container, press `Ctrl+C` if running in the foreground. If running in detached mode, use:

```bash
docker stop sentinel-ai
```

## Automated Testing

Run the project tests using pytest:

```bash
python -m pytest -v
```

The tests check application behavior and help identify errors before submission or further development.

## Jenkins Continuous Integration

The Jenkins pipeline is configured to:
1. Check the project files.
2. Run automated tests using pytest.
3. Report the pipeline result as SUCCESS or FAILURE.

This provides a basic Continuous Integration workflow. Docker image building and automatic deployment are not currently configured as Jenkins pipeline stages.

## Dataset
The project uses the SMS Spam Collection dataset stored in `SMSSpamCollection` to train and evaluate the spam classification model.

## Model Performance
The reported training accuracy is approximately **95.84%**. Training accuracy does not necessarily represent performance on unseen messages; independent test-set evaluation is recommended.

## Future Enhancements
- Add Selenium browser-based testing.
- Extend Jenkins to build and verify the Docker image automatically.
- Add model validation and retraining stages to the pipeline.
- Improve classification using additional datasets and model evaluation.
- Deploy the application to a cloud platform.




