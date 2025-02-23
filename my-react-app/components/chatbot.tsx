import React, { useState } from "react";
import "./chatbot.css";
import axios from "axios";

interface Message {
  text: string;
  sender: "user" | "bot";
}

const Chatbot: React.FC = () => {
  const [messages, setMessages] = useState<Message[]>([]);
  const [input, setInput] = useState("");

  const handleSendMessage = async () => {
    if (!input.trim()) return;

    const userMessage: Message = { text: input, sender: "user" };
    setMessages((prevMessages) => [...prevMessages, userMessage]);

    try {
      const response = await axios.post(
        `https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key=${import.meta.env.VITE_GEMINI_API_KEY}`,
        {
          contents: [{ parts: [{ text: input }] }]
        }
      );

      const botReply: string = response.data.candidates?.[0]?.content?.parts?.[0]?.text || "I couldn't find an answer.";
      const botMessage: Message = { text: botReply, sender: "bot" };

      setMessages((prevMessages) => [...prevMessages, botMessage]);
    } catch (error) {
      console.error("API Error:", error);
      setMessages((prevMessages) => [...prevMessages, { text: "Error getting response", sender: "bot" }]);
    }

    setInput("");
  };

  return (
    <div className="chat-container">
      <div className="chatbox">
        {messages.map((msg, index) => (
          <div key={index} className={`message ${msg.sender}`}>
            {msg.text}
          </div>
        ))}
      </div>
      <div className="input-container">
        <input
          type="text"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="Ask me anything about F1..."
        />
        <button onClick={handleSendMessage}>Send</button>
      </div>
    </div>
  );
};

export default Chatbot;
