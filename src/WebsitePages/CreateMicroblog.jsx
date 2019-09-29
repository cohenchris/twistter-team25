import React from "react";
import NavigationBar from "../components/NavigationBar";
import Editor from "../components/add-new-post/Editor";
import { otherDivStyle } from "..";

export default class CreateMicroblog extends React.Component {
  render() {
    return (
      <div className="CreateMicroblog" style={otherDivStyle}>
        <NavigationBar />
        <h1>CREATE A NEW MICROBLOG</h1>
        <Editor />
      </div>
    );
  }
}
