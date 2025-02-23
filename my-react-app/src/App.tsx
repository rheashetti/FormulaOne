import './App.css'

function App() {

  return (
    <>
      <div className = "navBar">
        <h1>Formula One Hub</h1>
        <div className = "navBar-links">
          <a href = "#home">Home</a>
          <a href = "#blog">Race Recaps</a>
          <a href = "#chabot">Formula 101</a>
          <a href = "#drivers">Driver Performance</a>
          <a href = "#pitstop">Pit Stop Performance</a>
        </div>
      </div>
      <div className = "home">
        <p>Welcome to the Formula One Hub! This is your one stop shop for all things Formula One.</p>
      </div>
    </>
  )
}

export default App
