# 🧠 Mindly - Emotion-Aware Chatbot (Mental Health Support)

Mindly is a Flask-based AI chatbot that is designed to provide mental health support by detecting emotions in user messages and generating empathetic responses based on those emotions. It leverages emotion detection models and GPT-3.5 for generating context-aware responses, creating a more human-like interaction for users seeking emotional support.

## 🚀 Features

- **Emotion Detection**: Automatically identifies emotions such as joy, sadness, anger, fear, and surprise.
- **Emotion-Based Response**: Dynamically generates empathetic replies using OpenAI GPT-3.5 based on the detected emotions.
- **Fallback Manual Detection**: In case of model failure, a basic keyword-based emotion detection method is used.
- **Real-Time Interaction**: Chat directly via terminal or connect via API.
- **CORS Enabled**: Allows easy connection with front-end frameworks such as React.js.

🛠 How It Works

User sends a message.
Emotion Detection: The message is processed using a Hugging Face model (distilroberta) to detect the underlying emotion.
Response Generation: Based on the detected emotion, an appropriate response is generated using GPT-3.5.
Send the response back to the user.

🧩 Models Used

Emotion Detection: j-hartmann/emotion-english-distilroberta-base
Response Generation: OpenAI GPT-3.5 (Chat Completion API)

Screenshots
<img width="1470" alt="Screenshot 2025-04-26 at 7 06 23 PM" src="https://github.com/user-attachments/assets/da19c42f-a2c8-439c-b9fc-23b31fd03efe" />

<img width="1463" alt="Screenshot 2025-04-26 at 7 06 33 PM" src="https://github.com/user-attachments/assets/9fef210a-dae0-47bb-bc4f-ad0812b70ce2" />

<img width="1462" alt="Screenshot 2025-04-26 at 7 06 40 PM" src="https://github.com/user-attachments/assets/88ec6515-c21e-4330-b63f-96fa421d5d7f" />

<img width="1468" alt="Screenshot 2025-04-26 at 7 16 36 PM" src="https://github.com/user-attachments/assets/c471dcc1-4d61-438b-a7d7-b97fb016f224" />

<img width="1460" alt="Screenshot 2025-04-26 at 7 16 55 PM" src="https://github.com/user-attachments/assets/09471394-f416-463c-bb33-c29d814db532" />


📝 Future Plans

Add conversation history/memory for more natural chats.
Customize responses for different severity levels (e.g., mild sadness vs. depression).
Support multiple languages for emotion detection and response.

🤝 Contributing

Contributions, suggestions, and pull requests are welcome! Feel free to open an issue to discuss changes or improvements.

📄 License

Licensed under the MIT License.

🎯 Key Takeaway

This is not just a chatbot. It is an emotionally aware AI system that understands how the user feels and responds accordingly to support mental health.

