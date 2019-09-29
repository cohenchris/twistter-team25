import React from "react";
import TwistterNav from "../components/TwistterNav";
export default class LoginPage extends React.Component {
  render() {
    return (
      <div className="LoginPage">
        <TwistterNav />
        <h1>Login Page!</h1>
        <h2>This page will display the login screen.</h2>
      </div>
    );
  }
}
