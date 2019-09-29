import React from "react";
import ReactDOM from "react-dom";
import "./index.css";
import * as serviceWorker from "./serviceWorker";
import "bootstrap/dist/css/bootstrap.min.css";
import "../node_modules/bootstrap/dist/css/bootstrap.min.css";
import StartPage from "./WebsitePages/StartPage/StartPage";
import AllTopics from "./WebsitePages/AllTopics";
import HomePage from "./WebsitePages/HomePage";

export const blogDivStyle = {
  marginLeft: "200px",
  marginRight: "200px"
};

ReactDOM.render(<HomePage />, document.getElementById("root"));

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA
serviceWorker.unregister();
