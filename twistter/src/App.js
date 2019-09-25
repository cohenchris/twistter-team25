import React from "react";
import ReactDOM from "react-dom";
import logo from "./Pictures/Logo.png";
import "./App.css";
import { BrowserRouter as Router, Switch, Route, Link } from "react-router-dom";
import * as ROUTES from "./constants/routes";
import LoginPage from "./LoginPage";

/* MAIN RENDER */
class App extends React.Component {
  render() {
    return (
      <Router>
        <div className="App">
          <HomePage />
          <Switch>
            <Route path={ROUTES.HOME} exact component={HomePage} />
            <Route path={ROUTES.LOGIN} component={LoginPage} />
          </Switch>
        </div>
      </Router>
    );
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
            <Router>
              <Link to={ROUTES.LOGIN}>
                <LoginButton />
              </Link>
            </Router>
          </p>
        </header>
      </div>
    );
  }
}

/* LOGIN BUTTON */
class LoginButton extends React.Component {
  handleClick() {
    ReactDOM.render(<LoginPage />, document.getElementById("root"));
  }

  render() {
    return <button onClick={this.handleClick}>Click here to login!</button>;
  }
}

export default App;
