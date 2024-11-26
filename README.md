# **Mindly - AI-powered Mental Health Support**

Mindly is a website designed to support mental well-being by providing users with a chatbot that responds according to emotional detection, offering diagnosis tests, and a variety of resources for mental health care. The platform uses cutting-edge AI technologies to enhance the mental health support experience.

## **Features**

Emotion Detection: The chatbot uses emotion detection powered by DistilRoBERTa to understand user emotions.

Response: The Gpt2 model is used to respond.

Diagnosis Test: Users can take mental health diagnosis tests to better understand their emotional and psychological well-being.

Resources for Mental Health: A library of resources is available, offering guidance and support for mental health issues.

Real-time Chatbot: A conversational interface that adapts its responses based on the user’s emotional state.

## **Tech Stack**

Frontend:
React: For building a responsive and interactive user interface.

Backend:
Flask: To handle server-side logic and API endpoints.

AI Models:
DistilRoBERTa: For emotion detection in user input.

## **Installation**

Clone the repository:
git clone https://github.com/your-username/mindly.git

Frontend Setup (React):
Navigate to the frontend directory:

cd frontend

Install dependencies:

npm install

Run the development server:

npm start

Backend Setup (Flask):

Navigate to the backend directory:

cd backend

Set up a virtual environment (optional but recommended):

python3 -m venv venv

source venv/bin/activate 

Install dependencies:

pip install -r requirements.txt

Run the Flask server:

python app.py

## **Dependencies:**

Flask: For backend development.

Transformers: For integrating the DistilRoBERTa model.

React: For the frontend user interface.

Other necessary libraries: Listed in requirements.txt for the backend.

## **Contributing**

We welcome contributions to Mindly! To contribute:

Fork this repository.
Create a new branch (git checkout -b feature-name).

Make your changes.

Commit your changes (git commit -am 'Add new feature').

Push to the branch (git push origin feature-name).

Open a pull request.

## **Team**

Tushar Swanskar

Rudra Pratap Tomer 



## **Acknowledgments**

DistilRoBERTa for emotion detection.

GPT2 model for response.

Flask for backend development.

React for frontend development.
