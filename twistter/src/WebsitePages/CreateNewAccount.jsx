import React from "react";
import TwistterNav from "../components/TwistterNav";

export default class CreateNewAccount extends React.Component {
  render() {
    return (
      <div className="CreateNewAccount">
        <TwistterNav />
        <h1>Create A New Account!</h1>
        <h4>
          This page will display editable text fields to create a new account
          for Twistter.
        </h4>
        <h4>TODO: Use hooks to make editable fields.</h4>
      </div>
    );
  }
}
