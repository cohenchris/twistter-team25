import React from "react";
import ReactDOM from "react-dom";
import "./CSSFiles/index.css";
import * as serviceWorker from "./serviceWorker";
import "bootstrap/dist/css/bootstrap.min.css";
import "../node_modules/bootstrap/dist/css/bootstrap.min.css";
import ProfileSettings from "./WebsitePages/ProfileSettings";
import StartPage from "./WebsitePages/StartPage";
import ProfilePage from "./WebsitePages/ProfilePage";
import LoginPage from "./WebsitePages/LoginPage";
import HomePage from "./WebsitePages/HomePage";
import DownForMaintenance from "./WebsitePages/DownForMaintenance";
import CreateANewPost from "./WebsitePages/CreateNewPost";
import CreateNewAccount from "./WebsitePages/CreateNewAccount";
import AllTopics from "./WebsitePages/AllTopics";

ReactDOM.render(<StartPage />, document.getElementById("root"));

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA
serviceWorker.unregister();
