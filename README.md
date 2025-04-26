
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Emotion-Aware Chatbot</title>
</head>

<body>
    <header>
        <h1>🧠Mindly- Emotion-Aware Chatbot (Mental Health Support)</h1>
        <p>This project is a Flask-based <strong>AI chatbot</strong> that:</p>
        <ul>
            <li><strong>Detects</strong> the emotion from the user's message.</li>
            <li><strong>Generates</strong> a smart, empathetic <strong>response based on the detected emotion</strong>.</li>
            <li>Combines <strong>emotion classification</strong> and <strong>GPT response generation</strong> for emotionally intelligent conversation.</li>
        </ul>
    </header>

    <section>
        <h2>🚀 Features</h2>
        <ul>
            <li><strong>Emotion Detection</strong>: Automatically identifies emotions like joy, sadness, anger, fear, surprise, etc.</li>
            <li><strong>Emotion-Based Response</strong>: Dynamically generates appropriate replies using OpenAI GPT-3.5 based on detected emotions.</li>
            <li><strong>Fallback Manual Detection</strong>: In case of model failure, basic keyword-based emotion detection is used.</li>
            <li><strong>Real-Time Interaction</strong>: Chat directly via terminal or connect via API.</li>
            <li><strong>CORS Enabled</strong>: Easy connection with frontends (e.g., React.js).</li>
        </ul>
    </section>

    <section>
        <h2>📂 Project Structure</h2>
        <pre>
mental-health-site/
├── model.py    # Flask backend server (Emotion detection + Response generation)
├── build/      # (Optional) Frontend build folder (if any frontend is added)
└── README.md   # Project documentation
        </pre>
    </section>

    <section>
        <h2>⚙️ Installation</h2>
        <ol>
            <li><strong>Clone the Repository</strong>
                <pre>git clone https://github.com/umanginigam/mental-health-chatbot.git
cd mental-health-site</pre>
            </li>
            <li><strong>Install Requirements</strong>
                <pre>pip install -r requirements.txt</pre>
            </li>
            <li><strong>Set Your OpenAI API Key</strong>
                <p>In <code>model.py</code>:</p>
                <pre>openai.api_key = "YOUR_OPENAI_API_KEY"</pre>
            </li>
            <li><strong>Run the Server</strong>
                <pre>python3 model.py</pre>
                <p>(Change port in <code>model.py</code> if needed, e.g., port=5001.)</p>
            </li>
        </ol>
    </section>

    <section>
        <h2>🛠️ How It Works</h2>
        <p>1. <strong>User sends a message</strong>.</p>
        <p>2. <strong>Emotion Detection</strong>: Use a Hugging Face model (<code>distilroberta</code>) to detect the underlying emotion.</p>
        <p>3. <strong>Response Generation</strong>: Based on the detected emotion, generate a suitable, empathetic response using GPT-3.5.</p>
        <p>4. <strong>Send the response back</strong>.</p>
    </section>

    <section>
        <h2>📡 API Usage</h2>
        <h3>Endpoint: <code>/chat</code></h3>
        <p><strong>Method</strong>: POST</p>
        <p><strong>URL</strong>: <code>http://localhost:5000/chat</code></p>
        <h4>Request Body:</h4>
        <pre>
{
  "message": "I feel anxious about my exams."
}
        </pre>
        <h4>Response Body:</h4>
        <pre>
{
  "response": "It’s completely normal to feel anxious before exams. You've prepared well, and you're going to do great!"
}
        </pre>
    </section>

    <section>
        <h2>🧩 Models Used</h2>
        <ul>
            <li><strong>Emotion Detection</strong>:  
                <a href="https://huggingface.co/j-hartmann/emotion-english-distilroberta-base">j-hartmann/emotion-english-distilroberta-base</a>
            </li>
            <li><strong>Response Generation</strong>:  
                OpenAI <code>gpt-3.5-turbo</code> (Chat Completion API)
            </li>
        </ul>
    </section>

    <section>
        <h2>⚠️ Common Issues and Fixes</h2>
        <table border="1">
            <tr>
                <th>Issue</th>
                <th>Solution</th>
            </tr>
            <tr>
                <td>Address already in use</td>
                <td>Kill previous process (<code>lsof -i :5000</code>, <code>kill -9 PID</code>) or change port</td>
            </tr>
            <tr>
                <td>return_all_scores warning</td>
                <td>Use <code>top_k=None</code> in pipeline</td>
            </tr>
            <tr>
                <td>GPU available but not used</td>
                <td>Set <code>device=0</code> in pipeline</td>
            </tr>
        </table>
    </section>
    <section>
    <h2>📸 Website Screenshots</h2>
    <p>Below are some screenshots of the website interface:</p>

    <!-- Screenshot 1 -->
    <img width="1470" alt="Screenshot 2025-04-26 at 7 06 23 PM" src="https://github.com/user-attachments/assets/e2908d75-53d0-4410-bfef-7d63dd7905e5" />


    <!-- Screenshot 2 -->
    <img width="1463" alt="Screenshot 2025-04-26 at 7 06 33 PM" src="https://github.com/user-attachments/assets/df1a6605-f77b-4ea1-bb55-7b5954e37060" />


    <!-- Screenshot 3 -->
    <img width="1462" alt="Screenshot 2025-04-26 at 7 06 40 PM" src="https://github.com/user-attachments/assets/da720f8e-069a-4d87-b09e-08f2b37a7bf0" />
    
    <img width="1468" alt="Screenshot 2025-04-26 at 7 16 36 PM" src="https://github.com/user-attachments/assets/bf500153-8b53-402c-a3fb-a49bbaf6b6d4" />
    
<img width="1460" alt="Screenshot 2025-04-26 at 7 16 55 PM" src="https://github.com/user-attachments/assets/3c3db9fb-8b09-4c16-9914-aeb428cb7fdf" />


</section>


    <section>
        <h2>🛠 Requirements</h2>
        <pre>
flask
transformers
torch
openai
flask-cors
        </pre>
        <p>(You can generate this by running <code>pip freeze > requirements.txt</code>.)</p>
    </section>

    <section>
        <h2>📝 Future Plans</h2>
        <ul>
            <li>Add a conversation history / memory to make chats more natural.</li>
            <li>Customize responses for different severity levels (e.g., mild sadness vs. depression).</li>
            <li>Support multiple languages for emotion detection and response.</li>
        </ul>
    </section>

    <section>
        <h2>🤝 Contributing</h2>
        <p>Contributions, suggestions, and pull requests are welcome!  
        Feel free to open an issue to discuss changes.</p>
    </section>

    <section>
        <h2>📄 License</h2>
        <p>Licensed under the <a href="LICENSE">MIT License</a>.</p>
    </section>

    <footer>
        <p>🎯 Key Takeaway: <strong>This is not just a chatbot. It is an emotionally aware AI system that understands how the user feels and responds accordingly to support mental health.</strong></p>
    </footer>

</body>

</html>

