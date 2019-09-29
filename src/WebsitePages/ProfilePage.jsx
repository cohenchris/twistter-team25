import React from "react";
import NavigationBar from "../components/NavigationBar";

export default class ProfilePage extends React.Component {
  render() {
    return (
      <div className="ProfilePage">
        <NavigationBar />
        <h1>Profile Page!</h1>
        <h2>
          This page will display the profile information of the current user.
        </h2>
      </div>
    );
  }
}
