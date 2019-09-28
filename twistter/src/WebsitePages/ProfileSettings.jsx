import React from "react";
import logo from "../Pictures/Logo.png";
export default class ProfileSettings extends React.Component {
  render() {
    return (
      <div>
        <img src={logo} className="App-logo" alt="logo" />
        <h1>Profile Settings!</h1>
      </div>
    );
  }
}
