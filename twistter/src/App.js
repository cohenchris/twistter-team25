import React from "react";
import logo from "./Pictures/Logo.png";
import "./CSSFiles/App.css";

/* MAIN RENDER */
class App extends React.Component {
  render() {
    return <HomePage />;
  }
}

/* HOME PAGE WITH LOGO AND LOGIN BUTTON */
class HomePage extends React.Component {
  render() {
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
}

/* LOGIN BUTTON */
class LoginButton extends React.Component {
  handleClick() {
    // GO TO LOGIN PAGE!
    /*ReactDOM.render(<LoginPage />, document.getElementById("root"));*/
  }

  render() {
    return <button onClick={this.handleClick}>Click here to login!</button>;
  }
}

export default App;
