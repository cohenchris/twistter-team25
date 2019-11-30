import React from "react";
import NavigationBar from "../../components/NavigationBar";
import PageTitle from "../../components/common/PageTitle";
import { blogDivStyle } from "../..";
import BlogPosts from "../../views/BlogPosts";

export default class Topic_Art extends React.Component {
  constructor(props) {
    super(props);
  }

  render() {
    return (
      <div className="MiscTopic" style={blogDivStyle}>
        <NavigationBar />
        <PageTitle
          sm="4"
          title="Blog Posts"
          //TODO: COMMUNICATE WITH API
          subtitle="Art"
          className="text-sm-left"
        />
        <BlogPosts topic="art" />
      </div>
    );
  }
}
