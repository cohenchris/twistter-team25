import React from "react";
import NavigationBar from "../../components/NavigationBar";
import PageTitle from "../../components/common/PageTitle";
import { blogDivStyle } from "../..";
import BlogPosts from "../../views/BlogPosts";

export default class AllTopics extends React.Component {
  render() {
    return (
      <div className="AllTopics" style={blogDivStyle}>
        <NavigationBar />
        <PageTitle
          sm="4"
          title="Blog Posts"
          subtitle="All Topics"
          className="text-sm-left"
        />
        <BlogPosts topic="all" />
      </div>
    );
  }
}
