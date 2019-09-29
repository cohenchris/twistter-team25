import React from "react";
import NavigationBar from "../components/NavigationBar";

export default class ProfileSettings extends React.Component {
  render() {
    return (
      <div className="ProfileSettings">
        <NavigationBar />
        <h1>Profile Settings!</h1>
        <h4>
          This page will display the profile/website settings of the current
          user.
        </h4>
      </div>
    );
  }
}
