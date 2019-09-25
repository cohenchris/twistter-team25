import React from "react";
import logo from "./Pictures/Logo.png";
import "./App.css";

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          <h1>Welcome to Twistter</h1>
          <h2>Go Team 25!</h2>
          <LoginButton />
        </p>
      </header>
    </div>
  );
}

class LoginButton extends React.Component {
  handleClick() {
    //TODO: redirect to the login screen
    alert("login redirect");
  }

  render() {
    return <button onClick={this.handleClick}>Click here to login!</button>;
  }
}
export default App;
