import React from "react";
import NavigationBar from "../components/NavigationBar";
import UserAccountDetails from "../components/user-profile-lite/UserAccountDetails";

export default class ProfileSettings extends React.Component {
  render() {
    return (
      <div className="ProfileSettings">
        <NavigationBar />
        <h1>PROFILE SETTINGS</h1>
        <UserAccountDetails />
      </div>
    );
  }
}
