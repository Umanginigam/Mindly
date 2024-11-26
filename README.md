# **Mindly - AI-powered Mental Health Support**

<img width="1470" alt="Screenshot 2024-11-26 at 4 54 33 PM" src="https://github.com/user-attachments/assets/9d5a1c88-7a1c-45de-9721-42a7bf6507c8">

Mindly is a website designed to support mental well-being by providing users with a chatbot that responds according to emotional detection, offering diagnosis tests, and a variety of resources for mental health care. The platform uses cutting-edge AI technologies to enhance the mental health support experience.

## **Features**

<img width="1470" alt="Screenshot 2024-11-26 at 7 02 12 PM" src="https://github.com/user-attachments/assets/91c29cd7-66b4-4a68-9d1b-46db71032319">

Emotion Detection: The chatbot uses emotion detection powered by DistilRoBERTa to understand user emotions.

Response: The Gpt2 model is used to respond.

Diagnosis Test: Users can take mental health diagnosis tests to better understand their emotional and psychological well-being.

<img width="1470" alt="Screenshot 2024-11-26 at 4 55 26 PM" src="https://github.com/user-attachments/assets/e1f3de38-551d-4f77-b716-7e9fca2714b4">

Resources for Mental Health: A library of resources is available, offering guidance and support for mental health issues.

<img width="1454" alt="Screenshot 2024-11-26 at 4 54 55 PM" src="https://github.com/user-attachments/assets/eb195ab1-7883-422c-9bea-6242675ea203">

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
