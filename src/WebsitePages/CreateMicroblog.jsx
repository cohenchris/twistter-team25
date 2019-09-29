import React from "react";
import NavigationBar from "../components/NavigationBar";
import Editor from "../components/add-new-post/Editor";

export default class CreateMicroblog extends React.Component {
  render() {
    return (
      <div className="CreateMicroblog">
        <NavigationBar />
        <h1>CREATE A NEW MICROBLOG</h1>
        <Editor />
      </div>
    );
  }
}
