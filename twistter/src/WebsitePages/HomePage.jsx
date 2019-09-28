import React from "react";
import logo from "../Pictures/Logo.png";
export default class HomePage extends React.Component {
  render() {
    return (
      <div>
        <img src={logo} className="App-logo" alt="logo" />
        <h1>Home Page!</h1>
      </div>
    );
  }
}
