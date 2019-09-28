import React from "react";
import logo from "../Pictures/Logo.png";
export default class DownForMaintenance extends React.Component {
  render() {
    return (
      <div>
        <img src={logo} className="App-logo" alt="logo" />
        <h1>We're Sorry, Twistter is Currently Down For Maintenance.</h1>
        <h2>Please Try Again Later.</h2>
      </div>
    );
  }
}
