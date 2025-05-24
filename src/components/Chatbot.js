// // src/Chatbot.js
// import React, { useState } from 'react';

// function Chatbot() {
//   const [message, setMessage] = useState('');
//   const [response, setResponse] = useState('');

//   const handleSubmit = async (event) => {
//     event.preventDefault();
    
//     const chatMessage = { message };  // Create the message object to send

//     try {
//       const res = await fetch('http://localhost:5000/chat', {
//         method: 'POST',
//         headers: {
//           'Content-Type': 'application/json',
//         },
//         body: JSON.stringify(chatMessage),
//       });
//       const data = await res.json();
      
//       if (data.response) {
//         setResponse(data.response);
//       } else if (data.error) {
//         setResponse(`Error: ${data.error}`);
//       }
//     } catch (error) {
//       setResponse(`Error: ${error.message}`);
//     }
//   };

//   return (
//     <div>
//       <h1>Chat with Chatbot</h1>
//       <form onSubmit={handleSubmit}>
//         <textarea
//           value={message}
//           onChange={(e) => setMessage(e.target.value)}
//           placeholder="Type your message..."
//           rows="4"
//           cols="50"
//         />
//         <button type="submit">Send</button>
//       </form>
//       <div>
//         <h3>Response:</h3>
//         <p>{response}</p>
//       </div>
//     </div>
//   );
// }

// export default Chatbot;

import React, { useState } from 'react';
import './Chatbot.css';

const Chatbot = () => {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState('');

  const handleSend = async () => {
    if (!input.trim()) return; 

    const newMessages = [...messages, { sender: 'user', text: input }];
    setMessages(newMessages);
    setInput('');

    try {
      // Send user input to the Flask API
      const response = await fetch('http://127.0.0.1:5000/chat', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ message: input }),
      });

      const data = await response.json();

      // Add the chatbot's response to the messages array
      if (data.response) {
        setMessages([...newMessages, { sender: 'bot', text: data.response }]);
      } else if (data.error) {
        setMessages([...newMessages, { sender: 'bot', text: `Error: ${data.error}` }]);
      }
    } catch (error) {
      console.error('Error communicating with API:', error);
      setMessages([...newMessages, { sender: 'bot', text: "I'm having trouble understanding. Please try again." }]);
    }
  }
  return (
    <div className="chatbot" id="chatbot">
      <h2>Chat with Mindly</h2>
      <div className="chat-window">
        <p>Hey, How you feel ?</p>
        {messages.map((msg, index) => (
          <div key={index} className={`chat-bubble ${msg.sender}`}>
            {msg.text}
          </div>
        ))}
      </div>
      <div className="chat-input">
        <input
          type="text"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="Type your message here..."
        />
        <button onClick={handleSend}>Send</button>
      </div>
    </div>
  );
};

export default Chatbot;
