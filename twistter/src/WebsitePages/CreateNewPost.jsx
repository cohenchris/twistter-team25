import React from "react";
import logo from "../Pictures/Logo.png";
export default class CreateANewPost extends React.Component {
  render() {
    return (
      <div>
        <img src={logo} className="App-logo" alt="logo" />
        <h1>Create A New Post!</h1>
      </div>
    );
  }
}
