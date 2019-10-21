import React from "react";
import ReactDOM from "react-dom";
import "./index.css";
import * as serviceWorker from "./serviceWorker";
import "bootstrap/dist/css/bootstrap.min.css";
import "../node_modules/bootstrap/dist/css/bootstrap.min.css";
import StartPage from "./WebsitePages/StartPage/StartPage";
import AllTopics from "./WebsitePages/AllTopics";
import CreateMicroblog from "./WebsitePages/CreateMicroblog";
import CreateNewAccount from "./WebsitePages/CreateNewAccount";
import DownForMaintenance from "./WebsitePages/DownForMaintenance";
import HomePage from "./WebsitePages/HomePage";
import LoginPage from "./WebsitePages/LoginPage";
import ProfilePage from "./WebsitePages/ProfilePage";
import ProfileSettings from "./WebsitePages/ProfileSettings";

export const blogDivStyle = {
  marginLeft: "200px",
  marginRight: "200px"
};

export const otherDivStyle = {
  marginLeft: "50px",
  marginRight: "50px"
};

ReactDOM.render(<CreateMicroblog />, document.getElementById("root"));

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA
serviceWorker.unregister();
