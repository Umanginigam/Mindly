# from flask import Flask, request, jsonify
# from transformers import pipeline
# from flask_cors import CORS
# import openai

# # Initialize emotion classification model
# emotion_classifier = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base", return_all_scores=True)

# app = Flask(__name__, static_folder='build')
# CORS(app)


# openai.api_key = ""

# # Emotion detection function (placeholder, replace with actual implementation)
# def detect_emotion(text):
#     # Dummy emotion detection logic for demonstration
#     # Replace this with your actual emotion detection model
#     if "happy" in text or "good" in text:
#         return "joy"
#     elif "sad" in text or "down" in text:
#         return "sadness"
#     elif "angry" in text or "mad" in text:
#         return "anger"
#     elif "surprised" in text or "shocked" in text:
#         return "surprise"
#     else:
#         return "neutral"

# # Generate emotional response using OpenAI's GPT
# def generate_emotional_response(user_input, emotion):
#     prompt = f"""
#     You are a chatbot that responds like a human. Your responses should match the detected emotion:
#     - Emotion: {emotion}
#     - User: {user_input}
#     - Chatbot:"""

#     response = openai.chat.completions.create(
#         model="gpt-3.5-turbo",
#         messages=[
#             {"role": "system", "content": "You are an empathetic chatbot."},
#             {"role": "user", "content": prompt}
#         ]
#     )
#     return response["choices"][0]["message"]["content"]

# # Interactive chatbot
# if __name__ == "__main__":
#     print("Chatbot: Hi there! How are you feeling today?")
#     while True:
#         user_input = input("You: ")  # Get user input
#         if user_input.lower() in ["exit", "quit"]:
#             print("Chatbot: Goodbye! Take care.")
#             break
#         emotion = detect_emotion(user_input)  # Detect emotion from user input
#         response = generate_emotional_response(user_input, emotion)  # Generate response
#         print(f"Chatbot: {response}")

# # Route for home page
# @app.route('/')
# def home():
#     return "Welcome to the Emotion and Intent-Based Chatbot API"


# @app.route('/chat', methods=['POST'])
# def chat():
#     try:
#         # Get user message from request JSON
#         user_message = request.json.get('message')
#         print(f"Received message: {user_message}")  # Debug log

#         if not user_message:
#             return jsonify({"error": "No message provided."}), 400

#         # Generate chatbot response
#         response = generate_response(user_message)
#         print(f"Generated response: {response}")  # Debug log

#         return jsonify({"response": response})
#     except Exception as e:
#         print(f"Error: {str(e)}")  # Debug log
#         return jsonify({"error": str(e)}), 500

# # Run the Flask app
# if __name__ == '__main__':
#     app.run(debug=True, port=5000)
from flask import Flask, request, jsonify
from transformers import pipeline
import random
from flask_cors import CORS

# Initialize emotion classification model
emotion_classifier = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base", return_all_scores=True)

app = Flask(__name__, static_folder='build')
CORS(app)
# Intent detection keywords
def detect_intent(user_input):
    breakup_keywords = [
        'breakup', 'broke up', 'relationship', 'heartbreak', 'separation',
        'split', 'divorce', 'ex', 'lost love', 'ended', 'cheating', 'betrayal',
        'argued', 'disagreement', 'left me', 'moving on', 'rejected', 'ghosted','cheated' ,'hurt','dhokha','dhoka',
    ]

    career_keywords = [
        'job', 'career', 'work', 'promotion', 'interview', 'boss', 'colleagues',
        'office', 'fired', 'hired', 'resignation', 'internship', 'offer',
        'pressure', 'stress', 'burnout'
    ]

    success_keywords = [
        'success', 'happy', 'achievement', 'achieve', 'won', 'victory', 'goal',
        'completed', 'promotion', 'celebrate', 'proud', 'reward', 'progress',
        'milestone', 'finished'
    ]

    # Detect intent based on keywords
    if any(word in user_input.lower() for word in breakup_keywords):
        return 'breakup'
    elif any(word in user_input.lower() for word in career_keywords):
        return 'career'
    elif any(word in user_input.lower() for word in success_keywords):
        return 'success'
    else:
        return 'general'

responses = {
    'breakup': {
        'sadness': [
            "Breakups can be tough. I'm here for you if you want to talk about it. 💔",
            "Take all the time you need to heal. You're not alone in this.🤗",
            "In life, everyone has difficult times, and you're dealing with this beautifully! 🌟",
            "Koi nahi, sab thik ho jayega. Vo tumhe deserve nahi karta tha! 💪❤",
            "It's okay to feel sad. Let yourself grieve and grow. 🌸",
            "Zindagi mein sabko mushkil waqt se guzarna padta hai, aur tum isse bohot achhe se handle kar rahe ho! 🌟",
            "Remember, the right person will never make you feel this way. 🕊️",
            "You deserve someone who values you completely. 🌟",
            "Healing takes time. Take one step at a time. 🧡",
            "It's okay to feel sad. Apne emotions ko samajhna zaroori hai. 🌸",
            "You’re not alone. I'm here to listen anytime you need.",
            "This chapter might be over, but your story is far from finished.",
            "Cry if you need to, but remember to smile again. 🌈",
            "Sometimes the hardest moments teach us the most valuable lessons.",
            "Focus on yourself—you deserve your own love and attention. 🌻",
            "One day, this will just be a memory of how strong you are.",
            "Healing mein time lagta hai. Ek step ek time par. 🧡",
            "The future holds beautiful surprises for you. Trust the journey.",
            "Lean on your friends and loved ones—they want to support you."
        ],
        'anger': [
            "I understand you're upset. Want to talk about what's bothering you?",
            "It's okay to feel angry. I'm here to listen if you want to vent.",
            "Anger is valid—let's channel it into something positive.",
            "Expressing your feelings is the first step to healing.",
            "You deserve peace; don’t let anyone take it away from you.",
            "What happened was unfair, but it doesn't define your worth.",
            "Channel this anger into growth—you're capable of amazing things.",
            "Your emotions are valid. Let’s work through them together.",
            "Anger can be empowering. Use it to set boundaries and grow.",
            "Don’t bottle it up. Speak your truth and let it out.",
            "I’m here for you—let me know how I can support you.",
            "Your strength shines even in moments of anger. 💪",
            "Take a deep breath. You’re doing the best you can.",
            "It's okay to be mad, but don’t let it consume you.",
            "Every storm passes. Let this be a lesson, not a limit.",
            "You’re worth more than the situation making you angry.",
            "Let’s turn this anger into a lesson you can grow from.",
            "Your feelings matter. Don’t hesitate to share them.",
            "Forgive, not for them, but for your own peace of mind.",
            "Remember, your energy is too precious to waste on anger."
        ],
        'joy': [
            "It seems like you're moving on positively. I'm happy for you!",
            "Stay strong and keep looking forward. Better days are ahead!",
            "Your smile says it all—you're doing great!",
            "Moving on is a brave step. You’re an inspiration! 🌟",
            "It’s wonderful to see you finding happiness again.",
            "You deserve every bit of joy coming your way. 🕊️",
            "Celebrate your strength—look how far you’ve come!",
            "The future looks bright, and you’re ready for it. 🌈",
            "Happiness suits you so well—keep shining!",
            "Life has so much more to offer, and you’re open to it.",
            "You’ve turned a tough situation into an opportunity to thrive.",
            "Seeing you joyful is a reminder that life is beautiful.",
            "Keep embracing the moments that bring you joy.",
            "Every step forward is worth celebrating. 🎉",
            "Let’s focus on the positives—you’re doing amazing!",
            "Your resilience is truly inspiring. Keep smiling!",
            "Joy looks good on you—keep being your radiant self.",
            "The strength you’ve shown is paving the way for your happiness.",
            "Your journey is inspiring, and this is just the beginning.",
            "Every day is a new chance to create more joy. 🌟"
        ],
        'neutral': [
            "Breakups can be challenging. How are you holding up?",
            "Focusing on yourself is important. What are you doing to feel better?",
            "This time is for you—rediscover what makes you happy.",
            "What’s on your mind? I’m here to listen.",
            "Take things one day at a time. You’ve got this.",
            "Have you tried any new hobbies or activities lately?",
            "It’s okay to take a step back and focus on you.",
            "Sometimes reflecting helps. Want to share your thoughts?",
            "What’s something positive you’ve done for yourself recently?",
            "This is a great time to invest in your personal growth.",
            "Every day is an opportunity to start fresh. What’s your plan?",
            "Let’s talk about how you can turn this into a positive change.",
            "Life is full of surprises—what’s next for you?",
            "Rediscovering yourself can be empowering. What excites you?",
            "This is your time to shine. What are your dreams?",
            "Let’s focus on your goals and how you can achieve them.",
            "You’re capable of so much—what’s your next step?",
            "Sometimes life redirects us for a reason. What’s your new path?",
            "Self-love is key. How are you nurturing yourself?",
            "This is the perfect time to prioritize your happiness."
        ]
    },
    'career': {
        'sadness': [
            "Work pressures can feel overwhelming. Take a moment to breathe.",
            "It's okay to feel this way. Want to share what's stressing you out?"
        ],
        'anger': [
            "Career struggles can be frustrating. What's bothering you?",
            "Work challenges happen to everyone. Let's figure it out together."
        ],
        'joy': [
            "Congratulations on your success! Tell me more about it!😊",
            "That's amazing! You deserve all the recognition. Keep going!"
        ],
        'neutral': [
            "Careers can be demanding. How can I help you today?",
            "What are your career goals? I'm here to support you!"
        ]
    },
    'success': {
        'joy': [
            "That's fantastic! How are you celebrating your achievement?",
            "Success looks great on you. Keep it up!"
        ],
        'neutral': [
            "Success is the result of your hard work. What’s next for you?",
            "Keep pushing forward—you’re doing great!"
        ]
    },
    'general': {
        'sadness': ["I'm here to listen. What's been bothering you?"],
        'anger': ["Take your time—I'm here to help if you want to talk about it."],
        'joy': ["I'm glad to see you happy! What's making you smile today? 😊"],
        'neutral': ["What’s on your mind? I’m here to chat!"]
    }
}

# Function to generate chatbot responses
def generate_response(user_input):
    # Classify emotion using the model
    emotions = emotion_classifier(user_input)
    detected_emotion = max(emotions[0], key=lambda x: x['score'])['label']
    
    # Detect intent based on user input
    intent = detect_intent(user_input)

    # Get response list for the detected intent and emotion
    intent_responses = responses.get(intent, {})
    emotion_responses = intent_responses.get(detected_emotion, ["I'm here for you."])
    
    # Pick a random response
    return random.choice(emotion_responses)

# Route for home page
@app.route('/')
def home():
    return "Welcome to the Emotion and Intent-Based Chatbot API"

@app.route('/chat', methods=['POST'])
def chat():
    try:
        # Get user message from request JSON
        user_message = request.json.get('message')
        print(f"Received message: {user_message}")  # Debug log

        if not user_message:
            return jsonify({"error": "No message provided"}), 400

        # Generate response using emotion and intent detection
        bot_response = generate_response(user_message)

        return jsonify({"response": bot_response})

    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"error": "Something went wrong on the server."}), 500


# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True, port=5001)