import React from "react";
import NavigationBar from "../components/NavigationBar";
import UserDetails from "../components/user-profile-lite/UserDetails";
import BlogPosts from "../views/BlogPosts";
import { otherDivStyle } from "..";

export default class ProfilePage extends React.Component {
  render() {
    return (
      <div className="ProfilePage" style={otherDivStyle}>
        <NavigationBar />
        <h1>PROFILE PAGE</h1>
        <UserDetails />
        <br></br>
        <br></br>
        <br></br>
        <h1>POSTS BY THIS USER</h1>
        {/*<BlogPosts />*/}
      </div>
    );
  }
}
