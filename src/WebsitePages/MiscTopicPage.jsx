import React from "react";
import NavigationBar from "../components/NavigationBar";
import PageTitle from "../components/common/PageTitle";
import { blogDivStyle } from "..";
import BlogPosts from "../views/BlogPosts";

export default class MiscTopicPage extends React.Component {
  constructor(props) {
    super(props);

    this.state = {
      // TODO: EVENTUALLY, THIS WILL BE THE TOPIC REQUESTED BY THE USER
      topic: props.topic
    };
  }

  render() {
    return (
      <div className="MiscTopic" style={blogDivStyle}>
        <NavigationBar />
        <PageTitle
          sm="4"
          title="Blog Posts"
          subtitle={this.state.topic}
          className="text-sm-left"
        />
        <BlogPosts />
      </div>
    );
  }
}
