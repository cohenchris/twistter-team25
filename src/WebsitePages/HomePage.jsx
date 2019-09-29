import React from "react";
import NavigationBar from "../components/NavigationBar";
import "bootstrap/dist/css/bootstrap.min.css";

export default class HomePage extends React.Component {
  render() {
    return (
      <div className="HomePage">
        <NavigationBar />
        <h1>Home Page!</h1>
        <h4>All followed topics will be displayed here...</h4>
      </div>
    );
  }
}
