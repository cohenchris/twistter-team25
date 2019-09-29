import React from "react";
import NavigationBar from "../components/NavigationBar";

export default class AllTopics extends React.Component {
  render() {
    return (
      <div className="AllTopics">
        <NavigationBar />
        <h1>#all</h1>
        <h4>
          This page will show all topics, regardless of what the user is
          following.
        </h4>
      </div>
    );
  }
}
