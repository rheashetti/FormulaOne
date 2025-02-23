import './App.css'
import React from 'react'
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom'
import Blog from '../components/blog'
import ChatBot from '../components/chatbot'
function App() {

  return (
    <Router>
      <div className = "navBar">
        <h1>Formula One Hub</h1>
        <div className = "navBar-links">
          <Link to="/">Home</Link>
          <Link to="/blog">Race Recaps</Link>
          <Link to="/chatbot">Formula 101</Link>
          <Link to="/drivers">Driver Performance</Link>
          <Link to="/pitstop">Pit Stop Simulator</Link>
        </div>
      </div>
      <Routes>
        {/*</Routes><Route path="/" element={<Home />} />*/}
        <Route path="/blog" element={<Blog />} />
        <Route path="/chatbot" element={<ChatBot />} />
      </Routes>
    </Router>
  );
}

export default App;
