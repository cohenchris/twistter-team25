import React from "react";
import NavigationBar from "../components/NavigationBar";
import UserDetails from "../components/user-profile-lite/UserDetails";

export default class ProfilePage extends React.Component {
  render() {
    return (
      <div className="ProfilePage">
        <NavigationBar />
        <h1>PROFILE PAGE</h1>
        <UserDetails />
      </div>
    );
  }
}
